-- ---------------------------------------------------------
-- ARCHIVO DE ESTRUCTURA DE BASE DE DATOS (schema.sql)
-- ---------------------------------------------------------

-- 1. LIMPIEZA PREVIA
-- El comando DROP TABLE elimina la tabla 'users' si ya existía.
-- Usamos esto para empezar "limpios" cada vez que iniciamos el sistema de cero.
DROP TABLE IF EXISTS users;

-- 2. CREACIÓN DE LA TABLA
-- El comando CREATE TABLE crea el "armario" donde guardaremos los datos.
CREATE TABLE users (
    
    -- Columna 'name': 
    -- TEXT: Guardará texto.
    -- PRIMARY KEY: Es la clave principal. Significa que NO se pueden repetir nombres.
    -- (Si intentas meter dos 'pepe', la base de datos dará error).
    name TEXT PRIMARY KEY,

    -- Columna 'email':
    -- TEXT: Guardará texto.
    -- NOT NULL: Significa que es obligatorio (no puedes guardar un usuario sin email).
    email TEXT NOT NULL
);

-- 3. DATOS DE PRUEBA (SEED DATA)
-- El comando INSERT INTO mete datos manualmente en la tabla.
-- Esto sirve para que cuando abras la web, ya haya algunos usuarios creados.

-- Insertamos al usuario 'admin'
INSERT INTO users (name, email) VALUES ('admin', 'admin@empresa.com');

-- Insertamos al usuario 'pepe'
INSERT INTO users (name, email) VALUES ('pepe', 'pepe@gmail.com');

-- Insertamos a la usuaria 'maria'
INSERT INTO users (name, email) VALUES ('maria', 'maria@hotmail.com');