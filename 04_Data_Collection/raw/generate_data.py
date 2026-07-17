import numpy as np
import pandas as pd
from datetime import date, timedelta
from faker import Faker
import math
import os

SEED = 42
np.random.seed(SEED)
fake = Faker("id_ID")
Faker.seed(SEED)

OUT_DIR = "/home/claude/raw"
os.makedirs(OUT_DIR, exist_ok=True)

TODAY = date(2026, 7, 17)

# 1. WAREHOUSES (15 cabang, Jawa & Sumatra, dengan koordinat kasar untuk hitung jarak antar rute pakai haversine)
warehouse_cities = [
    # (city, region, lat, lon)
    ("Jakarta",    "Jawa",     -6.2088, 106.8456),
    ("Bandung",    "Jawa",     -6.9175, 107.6191),
    ("Surabaya",   "Jawa",     -7.2575, 112.7521),
    ("Semarang",   "Jawa",     -6.9932, 110.4203),
    ("Yogyakarta", "Jawa",     -7.7956, 110.3695),
    ("Malang",     "Jawa",     -7.9666, 112.6326),
    ("Bekasi",     "Jawa",     -6.2383, 106.9756),
    ("Bogor",      "Jawa",     -6.5950, 106.8166),
    ("Tangerang",  "Jawa",     -6.1783, 106.6319),
    ("Depok",      "Jawa",     -6.4025, 106.7942),
    ("Medan",      "Sumatra",   3.5952,  98.6722),
    ("Palembang",  "Sumatra",  -2.9761, 104.7754),
    ("Padang",     "Sumatra",  -0.9471, 100.4172),
    ("Pekanbaru",  "Sumatra",   0.5071, 101.4478),
    ("Lampung",    "Sumatra",  -5.4292, 105.2610),
]

warehouses = []
for i, (city, region, lat, lon) in enumerate(warehouse_cities, start=1):
    warehouses.append({
        "warehouse_id": i,
        "warehouse_name": f"Cabang {city}",
        "city": city,
        "region": region,
        "daily_shipment_capacity": int(np.random.randint(300, 900)),
        "_lat": lat,
        "_lon": lon,
    })
df_warehouses = pd.DataFrame(warehouses)

# 2. COURIERS (300, di-assign ke salah satu warehouse)
vehicle_types = ["Motor", "Mobil Box", "Truk"]
vehicle_probs = [0.6, 0.3, 0.1]
vehicle_capacity_range = {
    "Motor": (15, 25),
    "Mobil Box": (30, 50),
    "Truk": (50, 80),
}

n_couriers = 300
courier_wh = np.random.choice(df_warehouses["warehouse_id"], size=n_couriers)
courier_vehicle = np.random.choice(vehicle_types, size=n_couriers, p=vehicle_probs)

couriers = []
for i in range(n_couriers):
    v = courier_vehicle[i]
    lo, hi = vehicle_capacity_range[v]
    couriers.append({
        "courier_id": i + 1,
        "courier_name": fake.name(),
        "warehouse_id": int(courier_wh[i]),
        "vehicle_type": v,
        "daily_delivery_capacity": int(np.random.randint(lo, hi + 1)),
    })
df_couriers = pd.DataFrame(couriers)

# 3. ROUTES (semua kombinasi origin -> destination antar cabang)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))

def delivery_days_from_distance(dist):
    if dist < 100:
        return 1
    elif dist < 300:
        return 2
    elif dist < 700:
        return 3
    elif dist < 1500:
        return 4
    else:
        return 6

routes = []
route_id = 1
wh_lookup = df_warehouses.set_index("warehouse_id")
for o_id in df_warehouses["warehouse_id"]:
    for d_id in df_warehouses["warehouse_id"]:
        if o_id == d_id:
            continue
        o = wh_lookup.loc[o_id]
        d = wh_lookup.loc[d_id]
        dist = haversine(o["_lat"], o["_lon"], d["_lat"], d["_lon"])
        dist = round(dist * np.random.uniform(1.05, 1.25), 1)  # faktor jalan darat, bukan garis lurus
        routes.append({
            "route_id": route_id,
            "origin_warehouse_id": int(o_id),
            "destination_warehouse_id": int(d_id),
            "distance_km": dist,
            "standard_delivery_days": delivery_days_from_distance(dist),
        })
        route_id += 1
df_routes = pd.DataFrame(routes)

# 4. CUSTOMERS (3000)
n_customers = 3000
extra_cities = ["Solo", "Cirebon", "Sidoarjo", "Batam", "Jambi", "Bengkulu"]
all_cities = [w[0] for w in warehouse_cities] + extra_cities

customers = []
for i in range(n_customers):
    customers.append({
        "customer_id": i + 1,
        "customer_name": fake.name(),
        "city": np.random.choice(all_cities),
        "customer_type": np.random.choice(["Individual", "Business"], p=[0.7, 0.3]),
    })
df_customers = pd.DataFrame(customers)

# 5. SHIPMENTS (8000, 6 bulan terakhir, delay dipengaruhi aturan bisnis)
n_shipments = 8000
start_date = TODAY - timedelta(days=182)  # ~6 bulan
date_range_days = (TODAY - start_date).days

# Bobot harian: musim ramai (Ramadan/Lebaran ~Feb-Mar 2026, sale 6.6 di Juni) lebih tinggi
day_list = [start_date + timedelta(days=i) for i in range(date_range_days + 1)]
day_weights = []
for d in day_list:
    w = 1.0
    if d.month in (2, 3):        # musim Ramadan/Lebaran
        w *= 1.8
    if d.month == 6 and 1 <= d.day <= 10:  # sale 6.6
        w *= 1.6
    day_weights.append(w)
day_weights = np.array(day_weights) / sum(day_weights)

shipment_dates = np.random.choice(day_list, size=n_shipments, p=day_weights)
customer_ids = np.random.choice(df_customers["customer_id"], size=n_shipments)
route_ids = np.random.choice(df_routes["route_id"], size=n_shipments)

route_lookup = df_routes.set_index("route_id")
origin_wh_for_route = route_lookup.loc[route_ids, "origin_warehouse_id"].values
distance_for_route = route_lookup.loc[route_ids, "distance_km"].values
std_days_for_route = route_lookup.loc[route_ids, "standard_delivery_days"].values

# Kurir dipilih dari warehouse asal rute
courier_by_wh = df_couriers.groupby("warehouse_id")["courier_id"].apply(list).to_dict()
courier_ids = np.array([
    np.random.choice(courier_by_wh[wh]) for wh in origin_wh_for_route
])

package_weight = np.round(np.random.lognormal(mean=1.1, sigma=0.7, size=n_shipments).clip(0.2, 60), 2)

df_ship = pd.DataFrame({
    "shipment_id": np.arange(1, n_shipments + 1),
    "customer_id": customer_ids,
    "courier_id": courier_ids,
    "route_id": route_ids,
    "shipment_date": shipment_dates,
    "package_weight_kg": package_weight,
    "distance_km": distance_for_route,
    "standard_delivery_days": std_days_for_route,
})
df_ship["shipment_date"] = pd.to_datetime(df_ship["shipment_date"]).dt.date
df_ship["estimated_delivery_date"] = df_ship.apply(
    lambda r: r["shipment_date"] + timedelta(days=int(r["standard_delivery_days"])), axis=1
)
df_ship["is_high_season"] = df_ship["shipment_date"].apply(
    lambda d: 1 if (d.month in (2, 3)) or (d.month == 6 and d.day <= 10) else 0
)

# Beban kurir per hari (semakin banyak shipment kurir yg sama, di hari yg sama -> makin sibuk)
courier_daily_load = df_ship.groupby(["courier_id", "shipment_date"])["shipment_id"].transform("count")
df_ship["courier_daily_load"] = courier_daily_load

# ---- Hitung probabilitas delay dari kombinasi faktor bisnis ----
dist_norm = (df_ship["distance_km"] - df_ship["distance_km"].min()) / (
    df_ship["distance_km"].max() - df_ship["distance_km"].min()
)
weight_norm = (df_ship["package_weight_kg"] - df_ship["package_weight_kg"].min()) / (
    df_ship["package_weight_kg"].max() - df_ship["package_weight_kg"].min()
)
load_norm = (df_ship["courier_daily_load"] - df_ship["courier_daily_load"].min()) / (
    df_ship["courier_daily_load"].max() - df_ship["courier_daily_load"].min() + 1e-9
)

base_delay_prob = 0.08
delay_prob = (
    base_delay_prob
    + 0.35 * dist_norm
    + 0.10 * weight_norm
    + 0.25 * load_norm
    + 0.15 * df_ship["is_high_season"]
)
delay_prob = delay_prob.clip(0.02, 0.90)

df_ship["_is_delayed"] = np.random.binomial(1, delay_prob)
extra_days = np.where(
    df_ship["_is_delayed"] == 1,
    np.random.randint(1, 6, size=n_shipments),
    0,
)
df_ship["actual_delivery_date"] = df_ship["estimated_delivery_date"] + pd.to_timedelta(extra_days, unit="D")
df_ship["shipment_status"] = np.where(
    df_ship["actual_delivery_date"] > df_ship["estimated_delivery_date"], "Delayed", "On-Time"
)

# ---- Biaya pengiriman: kombinasi jarak + berat + noise ----
rate_per_km = 800       # Rp per km
rate_per_kg = 3000      # Rp per kg
noise = np.random.normal(0, 5000, size=n_shipments)
df_ship["shipping_cost"] = (
    (df_ship["distance_km"] * rate_per_km) + (df_ship["package_weight_kg"] * rate_per_kg) + noise
).round(0).clip(lower=8000).astype(int)

df_shipments_final = df_ship[[
    "shipment_id", "customer_id", "courier_id", "route_id", "shipment_date",
    "package_weight_kg", "shipping_cost", "estimated_delivery_date",
    "actual_delivery_date", "shipment_status"
]].copy()

# Simpan ke CSV
df_warehouses_out = df_warehouses.drop(columns=["_lat", "_lon"])
df_warehouses_out.to_csv(f"{OUT_DIR}/warehouses.csv", index=False)
df_couriers.to_csv(f"{OUT_DIR}/couriers.csv", index=False)
df_routes.to_csv(f"{OUT_DIR}/routes.csv", index=False)
df_customers.to_csv(f"{OUT_DIR}/customers.csv", index=False)
df_shipments_final.to_csv(f"{OUT_DIR}/shipments.csv", index=False)

# Ringkasan validasi (dicetak ke console)
print("=== RINGKASAN DATA ===")
print(f"warehouses : {len(df_warehouses_out)} baris")
print(f"couriers   : {len(df_couriers)} baris")
print(f"routes     : {len(df_routes)} baris")
print(f"customers  : {len(df_customers)} baris")
print(f"shipments  : {len(df_shipments_final)} baris")
print()
overall_delay_rate = (df_shipments_final["shipment_status"] == "Delayed").mean()
print(f"Overall Delay Rate: {overall_delay_rate:.2%}")
print()

# Validasi pola: delay rate per kuartil jarak
q = pd.qcut(df_ship["distance_km"], 4, labels=["Q1 (dekat)", "Q2", "Q3", "Q4 (jauh)"])
print("Delay Rate per kuartil jarak:")
print(df_ship.groupby(q)["_is_delayed"].mean().round(3))
print()

print("Delay Rate: high season vs normal:")
print(df_ship.groupby("is_high_season")["_is_delayed"].mean().round(3))
print()

print("Delay Rate per kuartil beban kurir harian:")
ql = pd.qcut(df_ship["courier_daily_load"], 4, duplicates="drop")
print(df_ship.groupby(ql)["_is_delayed"].mean().round(3))
