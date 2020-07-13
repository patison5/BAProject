DROP TABLE IF EXISTS org_images;
DROP TABLE IF EXISTS srv_images;
DROP TABLE IF EXISTS pst_images;
DROP TABLE IF EXISTS trv_images;
DROP TABLE IF EXISTS msc_images;
DROP TABLE IF EXISTS posters;
DROP TABLE IF EXISTS travels;
DROP TABLE IF EXISTS misc;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS organizations;
DROP TABLE IF EXISTS images;

CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src TEXT NOT NULL,
    desc TEXT,
);

CREATE TABLE organizations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    image INTEGER NOT NULL,
    address TEXT NOT NULL,
    phones TEXT NOT NULL,
    email TEXT NOT NULL,
    link TEXT NOT NULL,
    barcode TEXT NOT NULL,
    timetable TEXT NOT NULL,
    FOREIGN KEY (image) REFERENCES images (id)
);

CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    organization_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    image INTEGER NOT NULL,
    address TEXT NOT NULL,
    phones TEXT NOT NULL,
    email TEXT NOT NULL,
    link TEXT NOT NULL,
    barcode TEXT NOT NULL,
    timetable TEXT NOT NULL,
    FOREIGN KEY (organization_id) REFERENCES organizations (id),
    FOREIGN KEY (image) REFERENCES images (id)
);

CREATE TABLE posters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    address TEXT NOT NULL,
    timetable TEXT NOT NULL,
    desc TEXT NOT NULL,
    image INTEGER,
    FOREIGN KEY (image) REFERENCES images (id)
);

CREATE TABLE travels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    address TEXT NOT NULL,
    timetable TEXT NOT NULL,
    desc TEXT NOT NULL,
    image INTEGER,
    FOREIGN KEY (image) REFERENCES images (id)
);

CREATE TABLE misc (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    endpoint TEXT NOT NULL,
    data TEXT NOT NULL
);

CREATE TABLE org_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_id INTEGER,
    organization_id INTEGER,
    FOREIGN KEY (image_id) REFERENCES images (id),
    FOREIGN KEY (organization_id) REFERENCES organizations (id)
);

CREATE TABLE srv_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_id INTEGER,
    service_id INTEGER,
    FOREIGN KEY (image_id) REFERENCES images (id),
    FOREIGN KEY (service_id) REFERENCES services (id)
);

CREATE TABLE pst_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_id INTEGER,
    poster_id INTEGER,
    FOREIGN KEY (image_id) REFERENCES images (id),
    FOREIGN KEY (poster_id) REFERENCES posters (id)
);

CREATE TABLE trv_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_id INTEGER,
    travel_id INTEGER,
    FOREIGN KEY (image_id) REFERENCES images (id),
    FOREIGN KEY (travel_id) REFERENCES travels (id)
);

CREATE TABLE msc_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_id INTEGER,
    misc_id INTEGER,
    FOREIGN KEY (image_id) REFERENCES images (id),
    FOREIGN KEY (misc_id) REFERENCES misc (id)
);