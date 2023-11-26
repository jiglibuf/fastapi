--
-- PostgreSQL database cluster dump
--

-- Started on 2023-11-26 19:50:43

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:KTLhWA8Z7B+GEs+jXIKehg==$IhyqdzQaOgQhQKFz7TEFpNpHtd+ts9Z6sPylY9T+UD4=:/uhADhnHUOpy+ZOtGSVsaC0ObT13RrSmVrwplawijfo=';

--
-- User Configurations
--








--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

-- Started on 2023-11-26 19:50:43

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

-- Completed on 2023-11-26 19:50:43

--
-- PostgreSQL database dump complete
--

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4
-- Dumped by pg_dump version 15.4

-- Started on 2023-11-26 19:50:43

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

--
-- TOC entry 2 (class 3079 OID 16384)
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- TOC entry 3368 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16398)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16520)
-- Name: bookings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bookings (
    id integer NOT NULL,
    room_id integer,
    user_id integer,
    date_from date NOT NULL,
    date_to date NOT NULL,
    price integer NOT NULL,
    total_cost integer GENERATED ALWAYS AS (((date_to - date_from) * price)) STORED,
    total_days integer GENERATED ALWAYS AS ((date_to - date_from)) STORED
);


ALTER TABLE public.bookings OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16519)
-- Name: bookings_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bookings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bookings_id_seq OWNER TO postgres;

--
-- TOC entry 3369 (class 0 OID 0)
-- Dependencies: 222
-- Name: bookings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bookings_id_seq OWNED BY public.bookings.id;


--
-- TOC entry 217 (class 1259 OID 16422)
-- Name: hotels; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hotels (
    id integer NOT NULL,
    name character varying NOT NULL,
    location character varying NOT NULL,
    services json,
    rooms_quantity integer NOT NULL,
    image_id integer
);


ALTER TABLE public.hotels OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16421)
-- Name: hotels_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hotels_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hotels_id_seq OWNER TO postgres;

--
-- TOC entry 3370 (class 0 OID 0)
-- Dependencies: 216
-- Name: hotels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hotels_id_seq OWNED BY public.hotels.id;


--
-- TOC entry 219 (class 1259 OID 16459)
-- Name: rooms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rooms (
    id integer NOT NULL,
    hotel_id integer NOT NULL,
    name character varying NOT NULL,
    description character varying,
    price integer NOT NULL,
    services json,
    quantity integer NOT NULL,
    image_id integer
);


ALTER TABLE public.rooms OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16458)
-- Name: rooms_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rooms_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.rooms_id_seq OWNER TO postgres;

--
-- TOC entry 3371 (class 0 OID 0)
-- Dependencies: 218
-- Name: rooms_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rooms_id_seq OWNED BY public.rooms.id;


--
-- TOC entry 221 (class 1259 OID 16492)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying NOT NULL,
    hashed_password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16491)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 3372 (class 0 OID 0)
-- Dependencies: 220
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3196 (class 2604 OID 16523)
-- Name: bookings id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bookings ALTER COLUMN id SET DEFAULT nextval('public.bookings_id_seq'::regclass);


--
-- TOC entry 3193 (class 2604 OID 16425)
-- Name: hotels id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hotels ALTER COLUMN id SET DEFAULT nextval('public.hotels_id_seq'::regclass);


--
-- TOC entry 3194 (class 2604 OID 16462)
-- Name: rooms id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rooms ALTER COLUMN id SET DEFAULT nextval('public.rooms_id_seq'::regclass);


--
-- TOC entry 3195 (class 2604 OID 16495)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3354 (class 0 OID 16398)
-- Dependencies: 215
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
06bdd906ce75
\.


--
-- TOC entry 3362 (class 0 OID 16520)
-- Dependencies: 223
-- Data for Name: bookings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bookings (id, room_id, user_id, date_from, date_to, price) FROM stdin;
1	1	1	2023-06-15	2023-06-30	24500
2	7	2	2023-06-25	2023-07-10	4300
3	2	5	2024-06-15	2024-06-30	22500
43	1	5	2024-02-15	2024-03-20	24500
44	2	5	2023-06-15	2023-06-20	22450
45	2	5	2023-06-15	2023-06-20	22450
46	1	5	2023-06-15	2023-06-20	24500
47	1	5	2023-06-15	2023-06-20	24500
\.


--
-- TOC entry 3356 (class 0 OID 16422)
-- Dependencies: 217
-- Data for Name: hotels; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hotels (id, name, location, services, rooms_quantity, image_id) FROM stdin;
1	Cosmos Collection Altay Resort	Республика Алтай, Майминский район, село Урлу-Аспак, Лесхозная улица, 20	["Wi-Fi", "Бассейн", "Парковка", "Кондиционер в номере"]	15	1
2	Skala	Республика Алтай, Майминский район, поселок Барангол, Чуйская улица 40а	["Wi-Fi", "Парковка"]	23	2
3	Ару-Кёль	Республика Алтай, Турочакский район, село Артыбаш, Телецкая улица, 44А	["Парковка"]	30	3
4	Гостиница Сыктывкар	Республика Коми, Сыктывкар, Коммунистическая улица, 67	["Wi-Fi", "Парковка", "Тренажёрный зал"]	55	4
5	Palace	Республика Коми, Сыктывкар, Первомайская улица, 62	["Wi-Fi", "Парковка", "Кондиционер в номере"]	22	5
6	Bridge Resort	посёлок городского типа Сириус, Фигурная улица, 45	["Wi-Fi", "Парковка", "Кондиционер в номере", "Тренажёрный зал"]	45	6
\.


--
-- TOC entry 3358 (class 0 OID 16459)
-- Dependencies: 219
-- Data for Name: rooms; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.rooms (id, hotel_id, name, description, price, services, quantity, image_id) FROM stdin;
1	1	Улучшенный с террасой и видом на озеро	Номер с видом на горы.	24500	["Бесплатный Wi‑Fi", "Кондиционер (с климат-контролем)"]	5	7
2	1	Делюкс Плюс	Шикарный номер с видом на озеро	22450	["Бесплатный Wi‑Fi", "Кондиционер"]	10	8
3	2	Номер на 2-х человек	Номер с видом на океан.	4570	[]	15	9
4	2	Номер на 3-х человек	Номер с видом на гору Тухтала.	4350	[]	8	10
5	3	Номер полулюкс семейный с 1 двуспальной кроватью	Красивый номер для всей семьи.	7080	["Холодильник"]	20	11
6	3	2-комнатный номер люкс комфорт	Красивый номер для молодоженов.	9815	[]	10	12
7	4	Стандарт двухместный	Стандартный номер для стандартных людей.	4300	["Бесплатный Wi‑Fi", "Холодильник"]	20	13
8	4	Стандарт улучшенный ПЛЮС	Номер для бурной вечеринки вдвоем.	4700	["Бесплатный Wi‑Fi", "Холодильник", "Ванная комната", "Кондиционер"]	35	14
9	5	Номер стандарт с 2 односпальными кроватями (с завтраком)	Вкусный завтрак и мягкий матрас - рецепт хорошего отдыха.	5000	[]	15	15
10	5	Номер полулюкс премиум (с завтраком)	Полулюкс - он и есть полулюкс, шик и блеск.	8000	[]	7	16
11	6	Стандарт (типовой корпус)	Стандартный номер.	8125	[]	45	17
\.


--
-- TOC entry 3360 (class 0 OID 16492)
-- Dependencies: 221
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, email, hashed_password) FROM stdin;
1	fedor@moloko.ru	tut_budet_hashed_password_1
2	sharik@moloko.ru	tut_budet_hashed_password_2
4	user@asd.com	$2b$12$0HnnnMcNCiqz2FFuXSZsFujaBnasA2o2ZvGazC9fj3iC1l5RqLQE.
5	user@example.com	$2b$12$QQ5rXi.SjM0fIcUGGWm2QeLi2X2M9OzSI2FBFvkmgP2GFqbqDNPKq
6	veiror300@gmail.com	$2b$12$TZF/egFO6INYZKtNograLepVUc63gKGt8jb5qYyRcgCgQMr4dW1TS
\.


--
-- TOC entry 3373 (class 0 OID 0)
-- Dependencies: 222
-- Name: bookings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bookings_id_seq', 49, true);


--
-- TOC entry 3374 (class 0 OID 0)
-- Dependencies: 216
-- Name: hotels_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hotels_id_seq', 6, true);


--
-- TOC entry 3375 (class 0 OID 0)
-- Dependencies: 218
-- Name: rooms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.rooms_id_seq', 11, true);


--
-- TOC entry 3376 (class 0 OID 0)
-- Dependencies: 220
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 6, true);


--
-- TOC entry 3200 (class 2606 OID 16402)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 3208 (class 2606 OID 16527)
-- Name: bookings bookings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bookings
    ADD CONSTRAINT bookings_pkey PRIMARY KEY (id);


--
-- TOC entry 3202 (class 2606 OID 16429)
-- Name: hotels hotels_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hotels
    ADD CONSTRAINT hotels_pkey PRIMARY KEY (id);


--
-- TOC entry 3204 (class 2606 OID 16466)
-- Name: rooms rooms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_pkey PRIMARY KEY (id);


--
-- TOC entry 3206 (class 2606 OID 16499)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3210 (class 2606 OID 16528)
-- Name: bookings bookings_room_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bookings
    ADD CONSTRAINT bookings_room_id_fkey FOREIGN KEY (room_id) REFERENCES public.rooms(id);


--
-- TOC entry 3211 (class 2606 OID 16533)
-- Name: bookings bookings_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bookings
    ADD CONSTRAINT bookings_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 3209 (class 2606 OID 16467)
-- Name: rooms rooms_hotel_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rooms
    ADD CONSTRAINT rooms_hotel_id_fkey FOREIGN KEY (hotel_id) REFERENCES public.hotels(id);


-- Completed on 2023-11-26 19:50:43

--
-- PostgreSQL database dump complete
--

-- Completed on 2023-11-26 19:50:43

--
-- PostgreSQL database cluster dump complete
--

