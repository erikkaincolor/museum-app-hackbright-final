--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Homebrew)
-- Dumped by pg_dump version 14.5 (Homebrew)

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
-- Name: art_faves; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.art_faves (
    id integer NOT NULL,
    patron_id integer NOT NULL,
    art_id integer NOT NULL
);


ALTER TABLE public.art_faves OWNER TO "Erikka";

--
-- Name: art_faves_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.art_faves_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.art_faves_id_seq OWNER TO "Erikka";

--
-- Name: art_faves_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.art_faves_id_seq OWNED BY public.art_faves.id;


--
-- Name: art_objects; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.art_objects (
    id integer NOT NULL,
    artist character varying(30) NOT NULL,
    title text NOT NULL,
    medium character varying(50) NOT NULL,
    description text NOT NULL,
    era character varying(30),
    img_path character varying,
    collection_id integer NOT NULL
);


ALTER TABLE public.art_objects OWNER TO "Erikka";

--
-- Name: art_objects_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.art_objects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.art_objects_id_seq OWNER TO "Erikka";

--
-- Name: art_objects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.art_objects_id_seq OWNED BY public.art_objects.id;


--
-- Name: collection_faves; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.collection_faves (
    id integer NOT NULL,
    patron_id integer NOT NULL,
    collection_id integer NOT NULL
);


ALTER TABLE public.collection_faves OWNER TO "Erikka";

--
-- Name: collection_faves_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.collection_faves_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.collection_faves_id_seq OWNER TO "Erikka";

--
-- Name: collection_faves_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.collection_faves_id_seq OWNED BY public.collection_faves.id;


--
-- Name: collections; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.collections (
    id integer NOT NULL,
    coll_category character varying(50),
    name text NOT NULL,
    description text,
    curator character varying(30) NOT NULL,
    era character varying(30)
);


ALTER TABLE public.collections OWNER TO "Erikka";

--
-- Name: collections_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.collections_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.collections_id_seq OWNER TO "Erikka";

--
-- Name: collections_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.collections_id_seq OWNED BY public.collections.id;


--
-- Name: collections_sounds; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.collections_sounds (
    id integer NOT NULL,
    collection_id integer NOT NULL,
    related_sound_id integer NOT NULL
);


ALTER TABLE public.collections_sounds OWNER TO "Erikka";

--
-- Name: collections_sounds_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.collections_sounds_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.collections_sounds_id_seq OWNER TO "Erikka";

--
-- Name: collections_sounds_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.collections_sounds_id_seq OWNED BY public.collections_sounds.id;


--
-- Name: museum_faves; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.museum_faves (
    id integer NOT NULL,
    patron_id integer NOT NULL,
    museum_id integer NOT NULL
);


ALTER TABLE public.museum_faves OWNER TO "Erikka";

--
-- Name: museum_faves_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.museum_faves_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.museum_faves_id_seq OWNER TO "Erikka";

--
-- Name: museum_faves_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.museum_faves_id_seq OWNED BY public.museum_faves.id;


--
-- Name: museums; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.museums (
    id integer NOT NULL,
    name text NOT NULL,
    street text NOT NULL,
    city character varying(20) NOT NULL,
    state character varying(20) NOT NULL,
    zipcode integer NOT NULL,
    weburl text NOT NULL
);


ALTER TABLE public.museums OWNER TO "Erikka";

--
-- Name: museums_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.museums_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.museums_id_seq OWNER TO "Erikka";

--
-- Name: museums_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.museums_id_seq OWNED BY public.museums.id;


--
-- Name: patrons; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.patrons (
    p_id integer NOT NULL,
    uname character varying(20) NOT NULL,
    fname character varying(20) NOT NULL,
    lname character varying(20) NOT NULL,
    email character varying(40) NOT NULL,
    pword character varying(10) NOT NULL
);


ALTER TABLE public.patrons OWNER TO "Erikka";

--
-- Name: patrons_p_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.patrons_p_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patrons_p_id_seq OWNER TO "Erikka";

--
-- Name: patrons_p_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.patrons_p_id_seq OWNED BY public.patrons.p_id;


--
-- Name: related_sound_faves; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.related_sound_faves (
    id integer NOT NULL,
    patron_id integer NOT NULL,
    related_sound_id integer NOT NULL
);


ALTER TABLE public.related_sound_faves OWNER TO "Erikka";

--
-- Name: related_sound_faves_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.related_sound_faves_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.related_sound_faves_id_seq OWNER TO "Erikka";

--
-- Name: related_sound_faves_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.related_sound_faves_id_seq OWNED BY public.related_sound_faves.id;


--
-- Name: related_sounds; Type: TABLE; Schema: public; Owner: Erikka
--

CREATE TABLE public.related_sounds (
    id integer NOT NULL,
    medium character varying(50) NOT NULL,
    sound_name text,
    description text NOT NULL,
    genre text,
    sound_source character varying,
    museum_id integer NOT NULL
);


ALTER TABLE public.related_sounds OWNER TO "Erikka";

--
-- Name: related_sounds_id_seq; Type: SEQUENCE; Schema: public; Owner: Erikka
--

CREATE SEQUENCE public.related_sounds_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.related_sounds_id_seq OWNER TO "Erikka";

--
-- Name: related_sounds_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Erikka
--

ALTER SEQUENCE public.related_sounds_id_seq OWNED BY public.related_sounds.id;


--
-- Name: art_faves id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.art_faves ALTER COLUMN id SET DEFAULT nextval('public.art_faves_id_seq'::regclass);


--
-- Name: art_objects id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.art_objects ALTER COLUMN id SET DEFAULT nextval('public.art_objects_id_seq'::regclass);


--
-- Name: collection_faves id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collection_faves ALTER COLUMN id SET DEFAULT nextval('public.collection_faves_id_seq'::regclass);


--
-- Name: collections id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collections ALTER COLUMN id SET DEFAULT nextval('public.collections_id_seq'::regclass);


--
-- Name: collections_sounds id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collections_sounds ALTER COLUMN id SET DEFAULT nextval('public.collections_sounds_id_seq'::regclass);


--
-- Name: museum_faves id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.museum_faves ALTER COLUMN id SET DEFAULT nextval('public.museum_faves_id_seq'::regclass);


--
-- Name: museums id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.museums ALTER COLUMN id SET DEFAULT nextval('public.museums_id_seq'::regclass);


--
-- Name: patrons p_id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.patrons ALTER COLUMN p_id SET DEFAULT nextval('public.patrons_p_id_seq'::regclass);


--
-- Name: related_sound_faves id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.related_sound_faves ALTER COLUMN id SET DEFAULT nextval('public.related_sound_faves_id_seq'::regclass);


--
-- Name: related_sounds id; Type: DEFAULT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.related_sounds ALTER COLUMN id SET DEFAULT nextval('public.related_sounds_id_seq'::regclass);


--
-- Data for Name: art_faves; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.art_faves (id, patron_id, art_id) FROM stdin;
1	1	1
\.


--
-- Data for Name: art_objects; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.art_objects (id, artist, title, medium, description, era, img_path, collection_id) FROM stdin;
1	Barbara Jones-Hogu	Nation Time	print	Barbara Jones-Hogu (American, 1938-2017). Nation Time, ca. 1970. Color screenprint, sheet: 22 1/2 x 30 in. (57.2 x 76.2 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.25. artist or artist's estate (Photo: Brooklyn Museum, 2012.80.25_PS4.jpg) 	Black Arts Movement	/static/img/c1-Nation-Time-Barbara-Jones-Hogu.jpg	1
2	Dindga McCannon	Empress Akweke	paint	 Dindga McCannon (American, born 1947). Empress Akweke, 1975. Acrylic on canvas, 35 7/8 × 31 15/16 × 13/16 in. (91.1 × 81.1 × 2.1 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.31. artist or artist's estate (Photo: Brooklyn Museum, 2012.80.31_PS9.jpg) 	Black Arts Movement	/static/img/c1-Nation-Time-Barbara-Jones-Hogu.jpg	1
3	Betye Saar	Liberation of Aunt Jemima: Cocktail	glass, paper, textile, metal	Betye Saar (American, born 1926). Liberation of Aunt Jemima: Cocktail, 1973. Glass, paper, textile, metal, Overall: 12 1/2 × 5 3/4 in. (31.8 × 14.6 cm). Brooklyn Museum, Purchased with funds given by Elizabeth A. Sackler, gift of the Contemporary Art Committee, and William K. Jacobs, Jr. Fund, 2017.17. © artist or artist's estate (Photo: , 2017.17_front_PS11.jpg) 	Black Arts Movement	/static/img/c1-Nation-Time-Barbara-Jones-Hogu.jpg	1
4	Tony Gleaton	Black Girl, White Flower, Belize, Central America	photograph	 Tony Gleaton (American, 1948-2015). Black Girl, White Flower, Belize, Central America, 1992. Gelatin silver photograph, image: 15 3/4 x 14 3/4 in. (40 x 37.5 cm). Brooklyn Museum, Gift of Helen Griffith in memory of Seymour Griffith, 1997.134. © artist or artist's estate (Photo: Brooklyn Museum, 1997.134_transp5713.jpg) 	Contemporary Art Movement	/static/img/c2-Glenn-Ligon-Crowd.jpg	2
5	Tony Gleaton	Un Hija de Jesus, Guatemala, Latin America, (Daughter of Jesus)	photograph	 Tony Gleaton (American, 1948-2015). Un Hija de Jesus, Guatemala, Latin America, (Daughter of Jesus), 1992. Gelatin silver photograph, image: 15 3/4 x 14 3/4 in. (40.0 x 37.5 cm). Brooklyn Museum, Purchased with funds given by Karen B. Cohen and Jan Staller, 1997.50. artist or artist's estate (Photo: Brooklyn Museum, 1997.50_bw.jpg)	Contemporary Art Movement	/static/img/c2-Glenn-Ligon-Crowd.jpg	2
6	Sarah A. Friedman	Untitled, Brooklyn, New York	photograph	Sarah A. Friedman (American). Untitled, Brooklyn, New York. Chromogenic photograph, Image: 19 1/2 x 15 1/2 in. (49.5 x 39.4 cm). Brooklyn Museum, Gift of the artist, 2001.110.2. Creative Commons-BY (Photo: Brooklyn Museum, 2001.110.2_bw.jpg) 	Contemporary Art Movement	/static/img/c2-Glenn-Ligon-Crowd.jpg	2
7	Nelson Stevens	Uhuru	print	Nelson Stevens (American, born 1938). Uhuru, 1971. Screenprint on paper, Sheet: 40 x 30 in. (101.6 x 76.2 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.41. artist or artist's estate (Photo: Brooklyn Museum, 2012.80.41_PS6.jpg) 	Black Arts Movement	/static/img/c3-Sarah-A-Friedman-Untitled.jpg	3
8	Marie Johnson Calloway	The Winner	print	Marie Johnson Calloway (American, 1920 - 2018). The Winner, 1971. Mixed media (acrylic, fabric) on wood, 60 x 30 in. (152.4 x 76.2 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.19. artist or artist's estate (Photo: Brooklyn Museum, CUR.2012.80.19.jpg) 	Black Arts Movement	/static/img/c3-Sarah-A-Friedman-Untitled.jpg	3
9	Glenn Ligon	[Untitled] (Crowd/The Fire Next Time)	print	The accumulation of crystals suggests the mass of participants in this historic event as viewed from above, while the juxtaposition of Baldwin’s words with the image of the march—separated by more than three decades—reminds us of the still-ongoing dialogue about race in America. Screenprint with coal crystals on paper, image: 12 × 18 1/8 in. (30.5 × 46 cm). Brooklyn Museum, Alfred T. White Fund, 2000.56. artist or artist's estate (Photo: Brooklyn Museum, 2000.56_transp5856.jpg)	Contemporary Art Movement	/static/img/c3-Sarah-A-Friedman-Untitled.jpg	3
10	Cleveland Bellow	George Jackson	print	Cleveland Bellow (American, 1946-2009). George Jackson, 1970. Screenprint on colored paper, Sheet: 23 1/2 x 17 1/2 in. (59.7 x 44.5 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.8. © artist or artist's estate (Photo: Brooklyn Museum, 2012.80.8_PS4.jpg)	Black Arts Movement	/static/img/c4-Cleveland-Bellow-George-Jackson.jpg	4
11	Cleveland Bellow	Untitled	print	Cleveland Bellow (American, 1946-2009). Untitled, 1968. Screenprint on paper, sheet: 19 1/2 x 15 1/4 in. (49.5 x 38.7 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.6. © artist or artist's estate (Photo: Brooklyn Museum, 2012.80.6_PS4.jpg)	Black Arts Movement	/static/img/c4-Cleveland-Bellow-George-Jackson.jpg	4
12	Cleveland Bellow	Duke	print	Cleveland Bellow (American, 1946-2009). Duke, 1968. Unique screenprint on two sheets of acrylic, Sheet: 28 x 22 in. (71.1 x 55.9 cm). Brooklyn Museum, Gift of R.M. Atwater, Anna Wolfrom Dove, Alice Fiebiger, Joseph Fiebiger, Belle Campbell Harriss, and Emma L. Hyde, by exchange, Designated Purchase Fund, Mary Smith Dorward Fund, Dick S. Ramsay Fund, and Carll H. de Silver Fund, 2012.80.7. artist or artist's estate (Photo: Brooklyn Museum, CUR.2012.80.7.jpg) 	Black Arts Movement	/static/img/c4-Cleveland-Bellow-George-Jackson.jpg	4
\.


--
-- Data for Name: collection_faves; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.collection_faves (id, patron_id, collection_id) FROM stdin;
\.


--
-- Data for Name: collections; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.collections (id, coll_category, name, description, curator, era) FROM stdin;
1	women	Awesome Black Radical Women, 1965–85	Women of color found themselves collaborating with and occasionally opposing the predominantly white, middle-class women who were primarily in charge of setting the tone, goals, and strategies for the battle for gender parity in the US during the second wave of feminism in the 1970s.	E. Polk	Spiral, Black Arts Movement
2	photography	Darkroom: Black and White Photos See the Light of Day	Photos of Black people from all over the diaspora, up close and in black and white.	E. Polk	Contemporary
3	mixed media	Contemporaries in Color	This collection displays African-Americna Art in the form of paint, mixed media and depicts people in natural state.	E. Polk	THE BLACK ARTS MOVEMENT
4	screenprint	Dip, Roll, and Print: Cleveland Bellow, American, 1946-2009	Cleveland Bellow portrayed Black musicians and activists in his graphic prints, as well as regular people like the young child in Untitled who is holding his hands behind his head. This piece subsequently became a billboard in Oakland, California as part of the national trend of public Black art.	E. Polk	Black Arts Movement
\.


--
-- Data for Name: collections_sounds; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.collections_sounds (id, collection_id, related_sound_id) FROM stdin;
1	1	1
2	2	2
3	3	3
4	4	4
\.


--
-- Data for Name: museum_faves; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.museum_faves (id, patron_id, museum_id) FROM stdin;
1	1	1
\.


--
-- Data for Name: museums; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.museums (id, name, street, city, state, zipcode, weburl) FROM stdin;
1	AFRICAN AMERICAN HERITAGE TRAIL	PO BOX 1827	MOBILE	AL	36633	HTTP://MVAFRICANAMERICANHERITAGETRAIL.ORG/
2	STATE BLACK ARCHIVES RESEARCH CENTER & MUSEUM	4900 MERIDIAN STREET NORTH	NORMAL	AL	35762	HTTP://WWW.AAMU.EDU/ADMINISTRATIVEOFFICES/LIBRARY/PAGES/STATE-BLACK-ARCHIVES-AND-RESEARCH-MUSEUM.ASPX
3	AFRICAN AMERICAN MULTICULTURAL MUSEUM	11259 E VIA LINDA SUITE 100-159	SCOTTSDALE	AZ	85259	HTTP://WWW.AAMMUSEUM.ORG
4	AFRICAN AMERICAN ART AND CULTURE	762 FULTON ST	SAN FRANCISCO	CA	94102	HTTP://WWW.AAACC.ORG/INDEX.HTML
5	AFRICAN AMERICAN FIREFIGHTER MUSEUM	1401 S CENTRAL AVE	LOS ANGELES	CA	90021	HTTP://WWW.AAFFMUSEUM.ORG
6	MUSEUM OF SAN DIEGO AFRICAN AMERICAN HISTORY	467 HORTON PLZ	SAN DIEGO	CA	92101	HTTP://WWW.AFRICANMUSEUMSANDIEGO.COM
7	CALIFORNIA AFRICAN AMERICAN MUSEUM	600 STATE DRIVE EXPOSIT	LOS ANGELES	CA	90037	HTTP://WWW.CAAMUSEUM.ORG/
8	MUSEUM OF AFRICAN AMERICAN ART	PO BOX 8418	LOS ANGELES	CA	90008	HTTP://WWW.MAAALA.ORG/
9	MUSEUM OF THE AFRICAN DIASPORA	685 MISSION ST	SAN FRANCISCO	CA	94105	HTTP://WWW.MOADSF.ORG
10	MUSEUM OF AFRICAN DIASPORA	90 NEW MONTGOMERY ST	SAN FRANCISCO	CA	94105	HTTP://WWW.MOADSF.ORG
11	ORAN Z'S PAN AFRICAN BLACK FACTS AND WAX MUSEUM	3742 W MARTIN LUTHER KING JR BLVD	LOS ANGELES	CA	90008	HTTP://WWW.ORANSBLACKMUSEUM.COM
12	STILES AFRICAN AMERICAN HERITAGE CENTER	2607 GLENARM PL	DENVER	CO	80205	HTTP://WWW.STILESHERITAGECENTER.ORG/
13	AFRICAN AMERICAN MUSEUM OF THE ARTS	PO BOX 1319	DELAND	FL	32721	HTTP://AFRICANMUSEUMDELAND.ORG/
14	SOUTHEASTERN REGIONAL BLACK ARCHIVES RESEARCH CENTER AND MUSEUM	445 GAMBLE ST	TALLAHASSEE	FL	32307	HTTP://WWW.FAMU.EDU/INDEX.CFM?BLACKARCHIVES
15	DR CARTER G WOODSON AFRICAN AMERICAN MUSEUM	2240 9TH AVE S	ST PETERSBURG	FL	33712	HTTP://WWW.WOODSONMUSEUM.ORG
16	LUCY CRAFT LANEY MUSEUM OF BLACK HISTORY	1116 PHILLIPS ST	AUGUSTA	GA	30901	HTTP://WWW.LUCYCRAFTLANEYMUSEUM.COM
17	TUBMAN AFRICAN AMERICAN MUSEUM	340 WALNUT ST	MACON	GA	31201	HTTP://WWW.TUBMANMUSEUM.COM
18	JIM-REE AFRICAN AMERICAN MUSEUM	PO BOX 6281	ELBERTON	GA	30635	HTTPS://JIMREE.ORG/
19	AFRICAN AMERICAN DIVERSITY CULTURAL CENTER HAWAII	1311 KAPIOLANI BLVD STE	HONOLULU	HI	96814	HTTP://WWW.AADCCH.ORG
20	AFRICAN AMERICAN HERITAGE FOUNDATION	PO BOX 2756	CEDAR RAPIDS	IA	52406	HTTP://WWW.BLACKIOWA.ORG
21	NATIONAL MUSEUM OF AFRICAN AMERICAN HISTORY AND CULTURE	PO BOX 1434	WATERLOO	IA	50704	HTTP://WWW.BLACKIOWA.ORG/
22	AFRICAN-AMERICAN HALL OF FAME MUSEUM	309 S DUSABLE ST	PEORIA	IL	61605	HTTP://AAHFMPEORIA.ORG
23	DUSABLE MUSEUM OF AFRICAN AMERICAN HISTORY	740 E 56TH PL	CHICAGO	IL	60637	HTTP://WWW.DUSABLEMUSEUM.ORG
24	AFRICAN-AMERICAN HERITAGE MUSEUM AND BLACK VETERAN'S ARCHIVES	1600 PHOENIX SQUARE	AURORA	IL	60505	HTTP://WWW.TAAHM.ORG/
25	KANSAS AFRICAN AMERICAN MUSEUM	601 N WATER ST	WICHITA	KS	67203	HTTP://TKAAMUSEUM.ORG
26	NEW ORLEANS AFRICAN AMERICAN MUSEUM OF ART CULTURE AND HISTORY (NOAAM)	1418 GOVERNOR NICHOLS ST	NEW ORLEANS	LA	70116	HTTP://NOAAM.ORG/
27	RIVER ROAD AFRICAN AMERICAN MUSEUM AND GALLERY	406 CHARLES ST	DONALDSONVLLE	LA	70346	HTTP://WWW.AFRICANAMERICANMUSEUM.ORG
28	ODELL S WILLIAMS NOW AND THEN AFRICAN AMERICAN	538 SOUTH BLVD	BATON ROUGE	LA	70802	HTTP://WWW.ATCHAFALAYA.ORG/404.HTML
29	TANGIPAHOA AFRICAN AMERICAN HERITAGE MUSEUM	1600 PHOENIX SQUARE	HAMMOND	LA	70403	HTTP://WWW.TAAHM.ORG
30	MUSEUM OF AFRICAN AMERICAN HISTORY AND CULTURE	13775 SOMERSET AVENUE	PRINCESS ANNE	MD	21853	HTTP://NMAAHC.SI.EDU/
31	BALTIMORE'S BLACK AMERICAN MUSEUM	1767 CARSWELL ST	BALTIMORE	MD	21218	HTTP://WWW.BBAM.BRAVEHOST.COM
32	GREAT BLACKS IN WAX MUSEUM	1601 E NORTH AVE	BALTIMORE	MD	21213	HTTP://WWW.GREATBLACKSINWAX.ORG
33	HOWARD COUNTY CENTER OF AFRICAN AMERICAN CULTURE	5434 VANTAGE POINT RD	COLUMBIA	MD	21044	HTTP://WWW.HCCAAC.ORG
34	PRINCE GEORGES AFRICAN AMERICAN MUSEUM	10201 MARTIN LUTHER KING JR HWY	BOWIE	MD	20720	HTTP://WWW.PGAAMCC.ORG/
35	AFRICAN AMERICAN SCHOOLHOUSE MUSEUM & HERITAGE COUNCIL	23620 NEWTON RD	WORTON	MD	21678	HTTPS://AFRICANAMERICANHERITAGECOUNCIL.SHUTTERFLY.COM/
36	AFRICAN AMERICAN COLLECTION OF MAINE	51 WESTMINSTER STREET	LEWISTON	ME	4240	HTTP://USM.MAINE.EDU/FRANCO
37	AFRICAN BEAD MUSEUM	6559 GRAND RIVER AVE	DETROIT	MI	48208	HTTP://MBAD.ORG
38	MUSEUM OF AFRICAN AMERICAN HISTORY	315 E WARREN AVE	DETROIT	MI	48201	HTTP://THEWRIGHT.ORG
39	MUSKEGON COUNTY MUSEUM OF AFRICAN AMERICAN HISTORY	2416 PECK ST	MUSKEGON HEIGHTS	MI	49444	HTTP://WWW.MUSEUMSUSA.ORG/MUSEUMS/INFO/16640
40	AFRICAN AMERICAN HISTORICAL & CIVIL RIGHTS MUSEUM	PO BOX 11302	MINNEAPOLIS	MN	55411	HTTP://WWW.MAAMCC.ORG/ABOUT-US/INDEX.PHP
41	MINNESOTA AFRICAN AMERICAN MUSEUM	1700 3RD AVE S	MINNEAPOLIS	MN	55404	HTTP://WWW.MAAMCC.ORG/INDEX.PHP
42	BLACK ARCHIVES OF MID-AMERICA	2033 VINE ST	KANSAS CITY	MO	64127	HTTP://BLACKARCHIVES.ORG/
43	*MUSEUM OF BLACK INVENTORS	5 SOUTH NEWSTEAD AVE	ST LOUIS	MO	63108	HTTP://BLACKINVENTOR.COM
44	OZARKS AFRICAN AMERICAN HERITAGE MUSEUM	PO BOX 265	ASH GROVE	MO	65604	HTTP://OAAHM.OMEKA.NET/
45	MUSEUM OF AFRICAN AMERICAN CULTURE	PO BOX 821956	VICKSBURG	MS	39182	HTTP://JACQUELINEHOUSE.WEEBLY.COM/INDEX.HTML
46	OAKES AFRICAN AMERICAN CULTURE CENTER	312 S MONROE ST	YAZOO CITY	MS	39194	HTTP://VISITYAZOO.ORG/OAKES-AFRICAN-AMERICAN-CULTURAL-CENTER/
47	AFRICAN AMERICAN MILITARY HISTORY MUSEUM	305 E 6TH ST	HATTIESBURG	MS	39401	HTTP://WWW.HATTIESBURGUSO.COM
48	REVEREND GEORGE LEE MUSEUMS OF AFRICAN AMERICAN HISTORY	17150 HIGHWAY 49	BELZONI	MS	39038	HTTP://WWW.THEFANNIELOUHAMERCIVILRIGHTSMUSEUM.COM/REV-GEORGE-W-LEE-MUSEUMS-OF-AFRICAN-AMERICAN-HISTORY-AND-HERITAGE.HTML
49	OAKES AFRICAN AMERICAN CULTURAL CENTER	312 S MONROE ST	YAZOO CITY	MS	39194	HTTP://WWW.VISITYAZOO.ORG/OAKES-AFRICAN-AMERICAN-CULTURAL-CENTER/
50	AFRICAN AMERICAN ATELIER	200 N DAVIE ST	GREENSBORO	NC	27401	HTTP://AFRICANAMERICANATELIER.ORG/
51	GREAT PLAINS BLACK MUSEUM AND INTERPRETIVE CENTER	1015 N 98TH STREET	OMAHA	NE	68114	HTTP://GPBLACKMUSEUM.ORG/
52	SEACOAST AFRICAN AMERICAN	PO BOX 4444	PORTSMOUTH	NH	3802	HTTP://SAACC-NH.ORG/
53	AFRICAN AMERICAN HERITAGE	661 JACKSON RD	HAMMONTON	NJ	8037	HTTP://WWW.AAHMSNJ.ORG/
54	AFRICAN AMERICAN HERITAGE MUSEUM OF SOUTHERN NEW JERSEY	702 N MICHIGAN AVE	ATLANTIC CITY	NJ	8401	HTTP://WWW.AAHMSNJ.ORG/
55	MUSEUM OF CONTEMPORARY AFRICAN DIASPORIAN ARTS	80 HANSON PLACE	BROOKLYN	NY	11217	HTTP://MOCADA.ORG/
56	SCHOMBURG CENTER FOR RESEARCH IN BLACK CULTURE	515 LENOX AVENUE	NEW YORK	NY	10037	HTTP://WWW.NYPL.ORG/LOCATIONS/SCHOMBURG
57	AFRICAN AMERICAN MUSEUM	1765 CRAWFORD ROAD	CLEVELAND	OH	44106	HTTP://WW4.AAMCLEVELAND.ORG/
58	REFLECTIONS IN BLACK MUSEUM	1314 DEEPWOOD DR	MACEDONIA	OH	44056	HTTP://WWW.REFLECTIONSINBLACKMUSEUM.COM
59	OKLAHOMA BLACK MUSEUM	4701 N LINCOLN BLVD	OKLAHOMA CITY	OK	73105	HTTP://WWW.OBMAPAC.ORG/
60	AFRICAN AMERICAN MUSEUM IN PHILADELPHIA	701 ARCH STREET	PHILADELPHIA	PA	19106	HTTP://WWW.AAMPMUSEUM.ORG
61	AVERY RESEARCH CENTER FOR AFRICAN AMERICAN HISTORY AND CULTURE	125 BULL STREET	CHARLESTON	SC	29424	HTTP://AVERY.COFC.EDU
62	CLEMSON AREA AFRICAN AMERICAN MUSEUM	PO BOX 145	CLEMSON	SC	29633	HTTP://CA-AAM.ORG/
63	INTERNATIONAL AFRICAN AMERICAN MUSEUM	284 KING ST # A	CHARLESTON	SC	29424	HTTP://WWW.IAAMUSEUM.ORG
64	SOUTH DAKOTA AFRICAN AMERICAN HISTORY MUSEUM	PO BOX 2266	SIOUX FALLS	SD	57101	HTTP://VISITSIOUXFALLS.COM/THINGS-TO-DO/ATTRACTIONS-AND-ENTERTAINMENT/DIRECTORY/AFRICAN-AMERICAN-HISTORY-MUSEUM/
65	BUFFALO SOLDIERS NATIONAL MUSEUM	3816 CAROLINE ST	HOUSTON	TX	77004	HTTP://BUFFALOSOLDIERMUSEUM.COM/
66	CALABOOSE AFRICAN AMERICAN MUSEUM	200 W MARTIN LUTHER KING DR	SAN MARCOS	TX	78666	HTTP://SANMARCOSARTS.COM
67	HOUSTON MUSEUM OF AFRICAN AMERICAN CULTURE	4807 CAROLINE ST	HOUSTON	TX	77004	HTTP://WWW.HMAAC.ORG
68	BLACK HISTORY MUSEUM AND CULTURAL CENTER	PO BOX 61052	RICHMOND	VA	23261	HTTP://BLACKHISTORYMUSEUM.ORG/
69	ALEXANDRIA BLACK HISTORY MUSEUM	902 WYTHE ST	ALEXANDRIA	VA	22314	HTTP://WWW.ALEXANDRIAVA.GOV/BLACKHISTORY
70	HARRISON MUSEUM OF AFRICAN AMERICAN CULTURE	523 HARRISON AVE	ROANOKE	VA	24026	HTTP://WWW.HARRISONMUSEUM.ORG
71	NORTHWEST AFRICAN AMERICAN MUSEUM	2300 S MASSACHUSSETTS ST	SEATTLE	WA	98144	HTTP://WWW.NAAMNW.ORG
\.


--
-- Data for Name: patrons; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.patrons (p_id, uname, fname, lname, email, pword) FROM stdin;
1	erikkaincolor	Erikka	Polk	erikkaincolor@gmail.com	1234
2	artistsmus3	Glenn	Ligon	glennlig0n@gmail.com	4321
3	solangel	Solange	Knowles	solange@gmail.com	abcd
\.


--
-- Data for Name: related_sound_faves; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.related_sound_faves (id, patron_id, related_sound_id) FROM stdin;
1	1	1
\.


--
-- Data for Name: related_sounds; Type: TABLE DATA; Schema: public; Owner: Erikka
--

COPY public.related_sounds (id, medium, sound_name, description, genre, sound_source, museum_id) FROM stdin;
1	podcast	7th chapel	gold foil walls	lively	/static/audio/test-door-sound.mp3	1
2	song	Luka Doncic speaks on...	yellow tinted scene	jittery	/static/audio/test-door-sound.mp3	2
3	playlist	Words from the curator	Spaghetti	novel	/static/audio/test-door-sound.mp3	3
4	commentary	At Last	baloons	n/a	/static/audio/test-door-sound.mp3	4
\.


--
-- Name: art_faves_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.art_faves_id_seq', 1, true);


--
-- Name: art_objects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.art_objects_id_seq', 12, true);


--
-- Name: collection_faves_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.collection_faves_id_seq', 2, true);


--
-- Name: collections_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.collections_id_seq', 4, true);


--
-- Name: collections_sounds_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.collections_sounds_id_seq', 4, true);


--
-- Name: museum_faves_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.museum_faves_id_seq', 2, true);


--
-- Name: museums_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.museums_id_seq', 71, true);


--
-- Name: patrons_p_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.patrons_p_id_seq', 3, true);


--
-- Name: related_sound_faves_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.related_sound_faves_id_seq', 1, true);


--
-- Name: related_sounds_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Erikka
--

SELECT pg_catalog.setval('public.related_sounds_id_seq', 4, true);


--
-- Name: art_faves art_faves_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.art_faves
    ADD CONSTRAINT art_faves_pkey PRIMARY KEY (id);


--
-- Name: art_objects art_objects_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.art_objects
    ADD CONSTRAINT art_objects_pkey PRIMARY KEY (id);


--
-- Name: art_objects art_objects_title_key; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.art_objects
    ADD CONSTRAINT art_objects_title_key UNIQUE (title);


--
-- Name: collection_faves collection_faves_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collection_faves
    ADD CONSTRAINT collection_faves_pkey PRIMARY KEY (id);


--
-- Name: collections collections_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collections
    ADD CONSTRAINT collections_pkey PRIMARY KEY (id);


--
-- Name: collections_sounds collections_sounds_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collections_sounds
    ADD CONSTRAINT collections_sounds_pkey PRIMARY KEY (id);


--
-- Name: museum_faves museum_faves_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.museum_faves
    ADD CONSTRAINT museum_faves_pkey PRIMARY KEY (id);


--
-- Name: museums museums_name_key; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.museums
    ADD CONSTRAINT museums_name_key UNIQUE (name);


--
-- Name: museums museums_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.museums
    ADD CONSTRAINT museums_pkey PRIMARY KEY (id);


--
-- Name: patrons patrons_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.patrons
    ADD CONSTRAINT patrons_pkey PRIMARY KEY (p_id);


--
-- Name: patrons patrons_uname_key; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.patrons
    ADD CONSTRAINT patrons_uname_key UNIQUE (uname);


--
-- Name: related_sound_faves related_sound_faves_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.related_sound_faves
    ADD CONSTRAINT related_sound_faves_pkey PRIMARY KEY (id);


--
-- Name: related_sounds related_sounds_pkey; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.related_sounds
    ADD CONSTRAINT related_sounds_pkey PRIMARY KEY (id);


--
-- Name: art_faves uc_art_faves; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.art_faves
    ADD CONSTRAINT uc_art_faves UNIQUE (patron_id, art_id);


--
-- Name: collection_faves uc_collection_faves; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collection_faves
    ADD CONSTRAINT uc_collection_faves UNIQUE (patron_id, collection_id);


--
-- Name: collections_sounds uc_collection_sounds; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collections_sounds
    ADD CONSTRAINT uc_collection_sounds UNIQUE (collection_id, related_sound_id);


--
-- Name: museum_faves uc_museum_faves; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.museum_faves
    ADD CONSTRAINT uc_museum_faves UNIQUE (patron_id, museum_id);


--
-- Name: related_sound_faves uc_sound_faves; Type: CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.related_sound_faves
    ADD CONSTRAINT uc_sound_faves UNIQUE (patron_id, related_sound_id);


--
-- Name: art_faves art_faves_art_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.art_faves
    ADD CONSTRAINT art_faves_art_id_fkey FOREIGN KEY (art_id) REFERENCES public.art_objects(id);


--
-- Name: art_faves art_faves_patron_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.art_faves
    ADD CONSTRAINT art_faves_patron_id_fkey FOREIGN KEY (patron_id) REFERENCES public.patrons(p_id);


--
-- Name: art_objects art_objects_collection_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.art_objects
    ADD CONSTRAINT art_objects_collection_id_fkey FOREIGN KEY (collection_id) REFERENCES public.collections(id);


--
-- Name: collection_faves collection_faves_collection_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collection_faves
    ADD CONSTRAINT collection_faves_collection_id_fkey FOREIGN KEY (collection_id) REFERENCES public.collections(id);


--
-- Name: collection_faves collection_faves_patron_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collection_faves
    ADD CONSTRAINT collection_faves_patron_id_fkey FOREIGN KEY (patron_id) REFERENCES public.patrons(p_id);


--
-- Name: collections_sounds collections_sounds_collection_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collections_sounds
    ADD CONSTRAINT collections_sounds_collection_id_fkey FOREIGN KEY (collection_id) REFERENCES public.collections(id);


--
-- Name: collections_sounds collections_sounds_related_sound_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.collections_sounds
    ADD CONSTRAINT collections_sounds_related_sound_id_fkey FOREIGN KEY (related_sound_id) REFERENCES public.related_sounds(id);


--
-- Name: museum_faves museum_faves_museum_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.museum_faves
    ADD CONSTRAINT museum_faves_museum_id_fkey FOREIGN KEY (museum_id) REFERENCES public.museums(id);


--
-- Name: museum_faves museum_faves_patron_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.museum_faves
    ADD CONSTRAINT museum_faves_patron_id_fkey FOREIGN KEY (patron_id) REFERENCES public.patrons(p_id);


--
-- Name: related_sound_faves related_sound_faves_patron_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.related_sound_faves
    ADD CONSTRAINT related_sound_faves_patron_id_fkey FOREIGN KEY (patron_id) REFERENCES public.patrons(p_id);


--
-- Name: related_sound_faves related_sound_faves_related_sound_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.related_sound_faves
    ADD CONSTRAINT related_sound_faves_related_sound_id_fkey FOREIGN KEY (related_sound_id) REFERENCES public.related_sounds(id);


--
-- Name: related_sounds related_sounds_museum_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Erikka
--

ALTER TABLE ONLY public.related_sounds
    ADD CONSTRAINT related_sounds_museum_id_fkey FOREIGN KEY (museum_id) REFERENCES public.museums(id);


--
-- PostgreSQL database dump complete
--

