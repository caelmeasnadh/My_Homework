--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    actor_name character varying(255),
    birth_date integer NOT NULL,
    number_of_movies integer DEFAULT 5 NOT NULL
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO postgres;

--
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- Name: directors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.directors (
    id integer NOT NULL,
    director_name character varying(255) NOT NULL,
    birth_date integer NOT NULL,
    director_number_of_movies integer DEFAULT 5 NOT NULL
);


ALTER TABLE public.directors OWNER TO postgres;

--
-- Name: directors_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.directors_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.directors_id_seq OWNER TO postgres;

--
-- Name: directors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.directors_id_seq OWNED BY public.directors.id;


--
-- Name: favorite_films; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.favorite_films (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    date_of_creation integer NOT NULL,
    rating integer DEFAULT 3 NOT NULL,
    viewed boolean DEFAULT true NOT NULL
);


ALTER TABLE public.favorite_films OWNER TO postgres;

--
-- Name: favorite_films_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.favorite_films_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.favorite_films_id_seq OWNER TO postgres;

--
-- Name: favorite_films_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.favorite_films_id_seq OWNED BY public.favorite_films.id;


--
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- Name: directors id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.directors ALTER COLUMN id SET DEFAULT nextval('public.directors_id_seq'::regclass);


--
-- Name: favorite_films id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.favorite_films ALTER COLUMN id SET DEFAULT nextval('public.favorite_films_id_seq'::regclass);


--
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actors (id, actor_name, birth_date, number_of_movies) FROM stdin;
1	Woody Harrelson	1961	23
3	Chirstian Bale	1974	23
4	Morgan Freeman	1937	23
2	Matthew McConaughey	1969	23
\.


--
-- Data for Name: directors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.directors (id, director_name, birth_date, director_number_of_movies) FROM stdin;
1	Matt Reeves	1966	5
2	Christopher Nolan	1970	5
3	Mary Harron	1953	5
4	David Fincher	1962	5
5	Baran bo Odar	1978	5
\.


--
-- Data for Name: favorite_films; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.favorite_films (id, name, date_of_creation, rating, viewed) FROM stdin;
2	Interstellar	2014	5	t
4	Seven	1995	5	t
6	Nightmare Alley	2021	5	t
3	American Psycho	2000	5	t
5	Dark	2017	5	t
1	Pans Labyrinth	2006	5	t
\.


--
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actors_id_seq', 6, true);


--
-- Name: directors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.directors_id_seq', 5, true);


--
-- Name: favorite_films_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.favorite_films_id_seq', 6, true);


--
-- PostgreSQL database dump complete
--

