--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.4
-- Dumped by pg_dump version 9.3.4
-- Started on 2014-06-16 05:51:00

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

DROP DATABASE mtgdb;
--
-- TOC entry 1968 (class 1262 OID 16394)
-- Name: mtgdb; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE mtgdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';


\connect mtgdb

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 5 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 1969 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 178 (class 3079 OID 11750)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 1971 (class 0 OID 0)
-- Dependencies: 178
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 171 (class 1259 OID 16397)
-- Name: cardinfo; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE cardinfo (
    gufy_id integer NOT NULL,
    id integer,
    name text,
    relatedcardid integer,
    setnumber integer,
    searchname text,
    description text,
    colors text[],
    manacost text,
    convertedmanacost integer,
    cardsetname text,
    type text,
    subtype text,
    power integer,
    toughness integer,
    loyalty integer,
    rarity text,
    artist text,
    cardsetid text,
    token boolean,
    rulings integer[],
    formats integer[],
    releasedat date,
    promo boolean,
    flavor text
);


--
-- TOC entry 170 (class 1259 OID 16395)
-- Name: cardinfo_gufy_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE cardinfo_gufy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1972 (class 0 OID 0)
-- Dependencies: 170
-- Name: cardinfo_gufy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE cardinfo_gufy_id_seq OWNED BY cardinfo.gufy_id;


--
-- TOC entry 177 (class 1259 OID 24624)
-- Name: formats; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE formats (
    gufy_id integer NOT NULL,
    name text,
    legality text,
    cardid integer
);


--
-- TOC entry 176 (class 1259 OID 24622)
-- Name: formats_gufy_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE formats_gufy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1973 (class 0 OID 0)
-- Dependencies: 176
-- Name: formats_gufy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE formats_gufy_id_seq OWNED BY formats.gufy_id;


--
-- TOC entry 175 (class 1259 OID 24593)
-- Name: rulings; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE rulings (
    gufy_id integer NOT NULL,
    releasedat date,
    rule text,
    cardid integer
);


--
-- TOC entry 174 (class 1259 OID 24591)
-- Name: rulings_gufy_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE rulings_gufy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1974 (class 0 OID 0)
-- Dependencies: 174
-- Name: rulings_gufy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE rulings_gufy_id_seq OWNED BY rulings.gufy_id;


--
-- TOC entry 172 (class 1259 OID 24576)
-- Name: sets; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE sets (
    gufy_id integer NOT NULL,
    id text,
    name text,
    type text,
    block text,
    description text,
    common integer,
    uncommon integer,
    rare integer,
    mythicrare integer,
    basicland integer,
    total integer,
    releasedat date,
    cardids integer[]
);


--
-- TOC entry 1975 (class 0 OID 0)
-- Dependencies: 172
-- Name: COLUMN sets.basicland; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON COLUMN sets.basicland IS '
';


--
-- TOC entry 173 (class 1259 OID 24579)
-- Name: sets_gufy_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE sets_gufy_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 1976 (class 0 OID 0)
-- Dependencies: 173
-- Name: sets_gufy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE sets_gufy_id_seq OWNED BY sets.gufy_id;


--
-- TOC entry 1845 (class 2604 OID 16400)
-- Name: gufy_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY cardinfo ALTER COLUMN gufy_id SET DEFAULT nextval('cardinfo_gufy_id_seq'::regclass);


--
-- TOC entry 1848 (class 2604 OID 24627)
-- Name: gufy_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY formats ALTER COLUMN gufy_id SET DEFAULT nextval('formats_gufy_id_seq'::regclass);


--
-- TOC entry 1847 (class 2604 OID 24596)
-- Name: gufy_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY rulings ALTER COLUMN gufy_id SET DEFAULT nextval('rulings_gufy_id_seq'::regclass);


--
-- TOC entry 1846 (class 2604 OID 24581)
-- Name: gufy_id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY sets ALTER COLUMN gufy_id SET DEFAULT nextval('sets_gufy_id_seq'::regclass);


--
-- TOC entry 1850 (class 2606 OID 16405)
-- Name: cardinfo_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY cardinfo
    ADD CONSTRAINT cardinfo_pk PRIMARY KEY (gufy_id);


--
-- TOC entry 1856 (class 2606 OID 24632)
-- Name: formats_id_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY formats
    ADD CONSTRAINT formats_id_pk PRIMARY KEY (gufy_id);


--
-- TOC entry 1854 (class 2606 OID 24601)
-- Name: ruling_id_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY rulings
    ADD CONSTRAINT ruling_id_pk PRIMARY KEY (gufy_id);


--
-- TOC entry 1852 (class 2606 OID 24589)
-- Name: sets_pk; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY sets
    ADD CONSTRAINT sets_pk PRIMARY KEY (gufy_id);


--
-- TOC entry 1970 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2014-06-16 05:51:01

--
-- PostgreSQL database dump complete
--

