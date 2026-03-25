DROP TABLE IF EXISTS aankoop;
DROP TABLE IF EXISTS transactie;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS filiaal;
DROP TABLE IF EXISTS bonuskaart;

CREATE TABLE bonuskaart(
bonuskaartnummer INTEGER PRIMARY KEY,
naam VARCHAR(255),
adres VARCHAR(255),
woonplaats VARCHAR(255)
);

CREATE TABLE filiaal(
filiaalnummer INTEGER PRIMARY KEY,
plaats VARCHAR(255) NOT NULL,
adres VARCHAR(255) NOT NULL
);

CREATE TABLE product(
productnummer INTEGER PRIMARY KEY,
omschrijving VARCHAR(255) NOT NULL,
prijs decimal(6,2) NOT NULL
);

CREATE TABLE transactie(
transactienummer SERIAL PRIMARY KEY,
datum DATE NOT NULL,
tijd TIME NOT NULL,
bonuskaartnummer INTEGER REFERENCES bonuskaart(bonuskaartnummer),
filiaalnummer INTEGER REFERENCES filiaal(filiaalnummer)
);

CREATE TABLE aankoop(
transactienummer INTEGER,
product INTEGER,
PRIMARY KEY (transactienummer, product),
FOREIGN KEY (transactienummer) REFERENCES transactie(transactienummer),
FOREIGN KEY (product) REFERENCES product(productnummer),
aantal INTEGER NOT NULL
);

INSERT INTO bonuskaart (bonuskaartnummer, naam, adres, woonplaats) VALUES
(65472335, NULL, NULL, NULL),
(12345678, 'Annette', 'Vredenburg 12', 'Utrecht'),
(98765, 'Jazim', 'Trekkerspad 5', 'Utrecht');

INSERT INTO filiaal (filiaalnummer, plaats, adres) VALUES
(35, 'Utrecht', 'Stationsplein 1'),
(48, 'Utrecht', 'Roelantdreef 41'),
(50, 'Utrecht', 'Biltstraat 90');

INSERT INTO product (productnummer, omschrijving, prijs) VALUES
(1, 'pak AH halfvolle melk', 0.99),
(2, 'pot AH pindakaas', 2.39),
(3, 'tandenborstel', 1.35),
(4, 'zak Lays ribbelchips paprika', 1.19),
(5, '2 kg handsinaasappels', 3.45);

INSERT INTO transactie (datum, tijd, bonuskaartnummer, filiaalnummer) VALUES
('2025-12-01', '17:35:00', 65472335, 35),
('2026-01-03', '12:25:00', 65472335, 48),
('2025-12-10', '08:30:00', 12345678, 35);

INSERT INTO aankoop (transactienummer, product, aantal) VALUES
(1, 1, 2),
(1, 2, 1),
(1, 3, 1),
(2, 1, 1),
(3, 1, 2);

SELECT f.filiaalnummer, adres, plaats, datum
FROM Filiaal AS f
INNER JOIN Transactie AS t ON t.filiaalnummer = f.filiaalnummer
WHERE t.bonuskaartnummer = 65472335;

SELECT SUM(prijs * aantal) AS totaalbedrag
FROM transactie AS t
INNER JOIN filiaal as f ON t.filiaalnummer = f.filiaalnummer
INNER JOIN aankoop AS a ON t.transactienummer = a.transactienummer
INNER JOIN product AS p ON a.product = p.productnummer
WHERE t.bonuskaartnummer = 65472335;

SELECT SUM(a.aantal) AS totaal
FROM filiaal AS f
INNER JOIN transactie AS t ON f.filiaalnummer = t.filiaalnummer
INNER JOIN aankoop AS a ON t.transactienummer = a.transactienummer
INNER JOIN product AS p ON a.product = p.productnummer
WHERE f.plaats = 'Utrecht'
AND p.omschrijving = 'pak AH halfvolle melk'
AND t.datum >= '2025-12-01'
AND t.datum < '2026-01-01';