CREATE TABLE IF NOT EXISTS import_runs (
  id TEXT PRIMARY KEY,
  started_at TEXT NOT NULL,
  completed_at TEXT,
  imported_by TEXT,
  ordem_filename TEXT NOT NULL,
  nota_filename TEXT NOT NULL,
  ordem_r2_key TEXT,
  nota_r2_key TEXT,
  status TEXT NOT NULL DEFAULT 'processing',
  expected_count INTEGER NOT NULL DEFAULT 0,
  processed_count INTEGER NOT NULL DEFAULT 0,
  valid_count INTEGER NOT NULL DEFAULT 0,
  error_count INTEGER NOT NULL DEFAULT 0,
  warning_count INTEGER NOT NULL DEFAULT 0,
  closed_count INTEGER NOT NULL DEFAULT 0,
  message TEXT
);

CREATE TABLE IF NOT EXISTS orders (
  order_no TEXT PRIMARY KEY,
  notification_no TEXT,
  notifier TEXT,
  created_by TEXT,
  entry_date TEXT NOT NULL,
  equipment TEXT,
  work_center TEXT,
  work_center_name TEXT,
  description TEXT,
  system_status TEXT,
  is_closed INTEGER NOT NULL DEFAULT 0,
  office_without_rc INTEGER NOT NULL DEFAULT 0,
  first_seen_at TEXT NOT NULL,
  last_seen_at TEXT NOT NULL,
  import_id TEXT NOT NULL,
  FOREIGN KEY(import_id) REFERENCES import_runs(id)
);

CREATE TABLE IF NOT EXISTS staging_orders (
  import_id TEXT NOT NULL,
  order_no TEXT NOT NULL,
  notification_no TEXT,
  notifier TEXT,
  created_by TEXT,
  entry_date TEXT NOT NULL,
  equipment TEXT,
  work_center TEXT,
  work_center_name TEXT,
  description TEXT,
  system_status TEXT,
  is_closed INTEGER NOT NULL DEFAULT 0,
  office_without_rc INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY(import_id, order_no),
  FOREIGN KEY(import_id) REFERENCES import_runs(id)
);

CREATE INDEX IF NOT EXISTS idx_orders_entry_date ON orders(entry_date);
CREATE INDEX IF NOT EXISTS idx_orders_open ON orders(is_closed);
CREATE INDEX IF NOT EXISTS idx_orders_notifier ON orders(notifier);
CREATE INDEX IF NOT EXISTS idx_orders_center ON orders(work_center);
CREATE INDEX IF NOT EXISTS idx_orders_equipment ON orders(equipment);
CREATE INDEX IF NOT EXISTS idx_staging_import ON staging_orders(import_id);
