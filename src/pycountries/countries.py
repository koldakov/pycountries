from enum import Enum

from pydantic import Field

from pycountries._base import EnumTypeBase, UnitBase


class CountryUnit(UnitBase):
    alpha_2: str = Field(
        min_length=2,
        max_length=2,
        description="A two-letter country code assigned to each country or territory in the ISO 3166-1 standard. "
        "These codes are used as part of domain names, vehicle registration plates, and in international "
        "transactions, among other purposes.",
        examples=[
            "US",
            "MT",
            "RU",
        ],
    )
    alpha_3: str = Field(
        min_length=3,
        max_length=3,
        description="A three-letter country code assigned to each country or territory in the ISO 3166-1 standard. "
        "These codes are commonly used in various international contexts, "
        "including identifying countries in internet domains, representing countries in airline "
        "ticketing, and facilitating international trade.",
        examples=[
            "USA",
            "MLT",
            "RUS",
        ],
    )
    numeric: str = Field(
        min_length=3,
        max_length=3,
        description="A three-digit numeric code assigned to each country or territory in the ISO 3166-1 standard. "
        "These codes are used in various contexts where numeric representations are preferred over "
        "alphanumeric ones, such as in databases or systems where numerical identifiers are "
        "easier to work with.",
        examples=[
            "840",
            "470",
            "643",
        ],
    )
    official_name: str = Field(
        description="Official country name,",
        examples=[
            "United States of America",
            "Republic of Malta",
            "Russian Federation",
        ],
    )
    name: str = Field(
        description="Country shorten name.",
        examples=[
            "United States",
            "Malta",
            "Russian Federation",
        ],
    )


class _CountryEnumType(EnumTypeBase):
    def __call__(cls, value, *args, **kw):  # noqa: N805
        _members = cls.__members__.values()  # type: ignore[var-annotated]
        country: Country
        for country in _members:
            if value in [
                country.alpha_2,
                country.alpha_3,
                country.numeric,
                int(country.numeric),
            ]:
                return country
        raise ValueError(f'"{value}" is not a valid {cls.__qualname__}') from None


class Country(Enum, metaclass=_CountryEnumType):
    """
    Country Enum, a comprehensive collection that incorporates essential identifiers according to the ISO 3166-1
    standard. It encompasses the ISO 3166-1 Alpha-2 code, which consists of two-letter country codes,
    the ISO 3166-1 Alpha-3 code, comprising three-letter country codes, and the ISO 3166-1 numeric code,
    which provides a three-digit numerical representation for each country.

    Additionally, the Country Enum includes the full country names corresponding to these codes, offering a complete
    reference for identifying and categorizing countries worldwide.
    """

    AW = CountryUnit(
        alpha_2="AW",
        alpha_3="ABW",
        numeric="533",
        name="Aruba",
        official_name="Aruba",
    )
    AF = CountryUnit(
        alpha_2="AF",
        alpha_3="AFG",
        numeric="004",
        name="Afghanistan",
        official_name="Islamic Republic of Afghanistan",
    )
    AO = CountryUnit(
        alpha_2="AO",
        alpha_3="AGO",
        numeric="024",
        name="Angola",
        official_name="Republic of Angola",
    )
    AI = CountryUnit(
        alpha_2="AI",
        alpha_3="AIA",
        numeric="660",
        name="Anguilla",
        official_name="Anguilla",
    )
    AX = CountryUnit(
        alpha_2="AX",
        alpha_3="ALA",
        numeric="248",
        name="Åland Islands",
        official_name="Åland Islands",
    )
    AL = CountryUnit(
        alpha_2="AL",
        alpha_3="ALB",
        numeric="008",
        name="Albania",
        official_name="Republic of Albania",
    )
    AD = CountryUnit(
        alpha_2="AD",
        alpha_3="AND",
        numeric="020",
        name="Andorra",
        official_name="Principality of Andorra",
    )
    AE = CountryUnit(
        alpha_2="AE",
        alpha_3="ARE",
        numeric="784",
        name="United Arab Emirates",
        official_name="United Arab Emirates",
    )
    AR = CountryUnit(
        alpha_2="AR",
        alpha_3="ARG",
        numeric="032",
        name="Argentina",
        official_name="Argentine Republic",
    )
    AM = CountryUnit(
        alpha_2="AM",
        alpha_3="ARM",
        numeric="051",
        name="Armenia",
        official_name="Republic of Armenia",
    )
    AS = CountryUnit(
        alpha_2="AS",
        alpha_3="ASM",
        numeric="016",
        name="American Samoa",
        official_name="American Samoa",
    )
    AQ = CountryUnit(
        alpha_2="AQ",
        alpha_3="ATA",
        numeric="010",
        name="Antarctica",
        official_name="Antarctica",
    )
    TF = CountryUnit(
        alpha_2="TF",
        alpha_3="ATF",
        numeric="260",
        name="French Southern Territories",
        official_name="French Southern Territories",
    )
    AG = CountryUnit(
        alpha_2="AG",
        alpha_3="ATG",
        numeric="028",
        name="Antigua and Barbuda",
        official_name="Antigua and Barbuda",
    )
    AU = CountryUnit(
        alpha_2="AU",
        alpha_3="AUS",
        numeric="036",
        name="Australia",
        official_name="Australia",
    )
    AT = CountryUnit(
        alpha_2="AT",
        alpha_3="AUT",
        numeric="040",
        name="Austria",
        official_name="Republic of Austria",
    )
    AZ = CountryUnit(
        alpha_2="AZ",
        alpha_3="AZE",
        numeric="031",
        name="Azerbaijan",
        official_name="Republic of Azerbaijan",
    )
    BI = CountryUnit(
        alpha_2="BI",
        alpha_3="BDI",
        numeric="108",
        name="Burundi",
        official_name="Republic of Burundi",
    )
    BE = CountryUnit(
        alpha_2="BE",
        alpha_3="BEL",
        numeric="056",
        name="Belgium",
        official_name="Kingdom of Belgium",
    )
    BJ = CountryUnit(
        alpha_2="BJ",
        alpha_3="BEN",
        numeric="204",
        name="Benin",
        official_name="Republic of Benin",
    )
    BQ = CountryUnit(
        alpha_2="BQ",
        alpha_3="BES",
        numeric="535",
        name="Bonaire, Sint Eustatius and Saba",
        official_name="Bonaire, Sint Eustatius and Saba",
    )
    BF = CountryUnit(
        alpha_2="BF",
        alpha_3="BFA",
        numeric="854",
        name="Burkina Faso",
        official_name="Burkina Faso",
    )
    BD = CountryUnit(
        alpha_2="BD",
        alpha_3="BGD",
        numeric="050",
        name="Bangladesh",
        official_name="People's Republic of Bangladesh",
    )
    BG = CountryUnit(
        alpha_2="BG",
        alpha_3="BGR",
        numeric="100",
        name="Bulgaria",
        official_name="Republic of Bulgaria",
    )
    BH = CountryUnit(
        alpha_2="BH",
        alpha_3="BHR",
        numeric="048",
        name="Bahrain",
        official_name="Kingdom of Bahrain",
    )
    BS = CountryUnit(
        alpha_2="BS",
        alpha_3="BHS",
        numeric="044",
        name="Bahamas",
        official_name="Commonwealth of the Bahamas",
    )
    BA = CountryUnit(
        alpha_2="BA",
        alpha_3="BIH",
        numeric="070",
        name="Bosnia and Herzegovina",
        official_name="Republic of Bosnia and Herzegovina",
    )
    BL = CountryUnit(
        alpha_2="BL",
        alpha_3="BLM",
        numeric="652",
        name="Saint Barthélemy",
        official_name="Saint Barthélemy",
    )
    BY = CountryUnit(
        alpha_2="BY",
        alpha_3="BLR",
        numeric="112",
        name="Belarus",
        official_name="Republic of Belarus",
    )
    BZ = CountryUnit(
        alpha_2="BZ",
        alpha_3="BLZ",
        numeric="084",
        name="Belize",
        official_name="Belize",
    )
    BM = CountryUnit(
        alpha_2="BM",
        alpha_3="BMU",
        numeric="060",
        name="Bermuda",
        official_name="Bermuda",
    )
    BO = CountryUnit(
        alpha_2="BO",
        alpha_3="BOL",
        numeric="068",
        name="Bolivia, Plurinational State of",
        official_name="Plurinational State of Bolivia",
    )
    BR = CountryUnit(
        alpha_2="BR",
        alpha_3="BRA",
        numeric="076",
        name="Brazil",
        official_name="Federative Republic of Brazil",
    )
    BB = CountryUnit(
        alpha_2="BB",
        alpha_3="BRB",
        numeric="052",
        name="Barbados",
        official_name="Barbados",
    )
    BN = CountryUnit(
        alpha_2="BN",
        alpha_3="BRN",
        numeric="096",
        name="Brunei Darussalam",
        official_name="Brunei Darussalam",
    )
    BT = CountryUnit(
        alpha_2="BT",
        alpha_3="BTN",
        numeric="064",
        name="Bhutan",
        official_name="Kingdom of Bhutan",
    )
    BV = CountryUnit(
        alpha_2="BV",
        alpha_3="BVT",
        numeric="074",
        name="Bouvet Island",
        official_name="Bouvet Island",
    )
    BW = CountryUnit(
        alpha_2="BW",
        alpha_3="BWA",
        numeric="072",
        name="Botswana",
        official_name="Republic of Botswana",
    )
    CF = CountryUnit(
        alpha_2="CF",
        alpha_3="CAF",
        numeric="140",
        name="Central African Republic",
        official_name="Central African Republic",
    )
    CA = CountryUnit(
        alpha_2="CA",
        alpha_3="CAN",
        numeric="124",
        name="Canada",
        official_name="Canada",
    )
    CC = CountryUnit(
        alpha_2="CC",
        alpha_3="CCK",
        numeric="166",
        name="Cocos (Keeling) Islands",
        official_name="Cocos (Keeling) Islands",
    )
    CH = CountryUnit(
        alpha_2="CH",
        alpha_3="CHE",
        numeric="756",
        name="Switzerland",
        official_name="Swiss Confederation",
    )
    CL = CountryUnit(
        alpha_2="CL",
        alpha_3="CHL",
        numeric="152",
        name="Chile",
        official_name="Republic of Chile",
    )
    CN = CountryUnit(
        alpha_2="CN",
        alpha_3="CHN",
        numeric="156",
        name="China",
        official_name="People's Republic of China",
    )
    CI = CountryUnit(
        alpha_2="CI",
        alpha_3="CIV",
        numeric="384",
        name="Côte d'Ivoire",
        official_name="Republic of Côte d'Ivoire",
    )
    CM = CountryUnit(
        alpha_2="CM",
        alpha_3="CMR",
        numeric="120",
        name="Cameroon",
        official_name="Republic of Cameroon",
    )
    CD = CountryUnit(
        alpha_2="CD",
        alpha_3="COD",
        numeric="180",
        name="Congo, The Democratic Republic of the",
        official_name="Congo, The Democratic Republic of the",
    )
    CG = CountryUnit(
        alpha_2="CG",
        alpha_3="COG",
        numeric="178",
        name="Congo",
        official_name="Republic of the Congo",
    )
    CK = CountryUnit(
        alpha_2="CK",
        alpha_3="COK",
        numeric="184",
        name="Cook Islands",
        official_name="Cook Islands",
    )
    CO = CountryUnit(
        alpha_2="CO",
        alpha_3="COL",
        numeric="170",
        name="Colombia",
        official_name="Republic of Colombia",
    )
    KM = CountryUnit(
        alpha_2="KM",
        alpha_3="COM",
        numeric="174",
        name="Comoros",
        official_name="Union of the Comoros",
    )
    CV = CountryUnit(
        alpha_2="CV",
        alpha_3="CPV",
        numeric="132",
        name="Cabo Verde",
        official_name="Republic of Cabo Verde",
    )
    CR = CountryUnit(
        alpha_2="CR",
        alpha_3="CRI",
        numeric="188",
        name="Costa Rica",
        official_name="Republic of Costa Rica",
    )
    CU = CountryUnit(
        alpha_2="CU",
        alpha_3="CUB",
        numeric="192",
        name="Cuba",
        official_name="Republic of Cuba",
    )
    CW = CountryUnit(
        alpha_2="CW",
        alpha_3="CUW",
        numeric="531",
        name="Curaçao",
        official_name="Curaçao",
    )
    CX = CountryUnit(
        alpha_2="CX",
        alpha_3="CXR",
        numeric="162",
        name="Christmas Island",
        official_name="Christmas Island",
    )
    KY = CountryUnit(
        alpha_2="KY",
        alpha_3="CYM",
        numeric="136",
        name="Cayman Islands",
        official_name="Cayman Islands",
    )
    CY = CountryUnit(
        alpha_2="CY",
        alpha_3="CYP",
        numeric="196",
        name="Cyprus",
        official_name="Republic of Cyprus",
    )
    CZ = CountryUnit(
        alpha_2="CZ",
        alpha_3="CZE",
        numeric="203",
        name="Czechia",
        official_name="Czech Republic",
    )
    DE = CountryUnit(
        alpha_2="DE",
        alpha_3="DEU",
        numeric="276",
        name="Germany",
        official_name="Federal Republic of Germany",
    )
    DJ = CountryUnit(
        alpha_2="DJ",
        alpha_3="DJI",
        numeric="262",
        name="Djibouti",
        official_name="Republic of Djibouti",
    )
    DM = CountryUnit(
        alpha_2="DM",
        alpha_3="DMA",
        numeric="212",
        name="Dominica",
        official_name="Commonwealth of Dominica",
    )
    DK = CountryUnit(
        alpha_2="DK",
        alpha_3="DNK",
        numeric="208",
        name="Denmark",
        official_name="Kingdom of Denmark",
    )
    DO = CountryUnit(
        alpha_2="DO",
        alpha_3="DOM",
        numeric="214",
        name="Dominican Republic",
        official_name="Dominican Republic",
    )
    DZ = CountryUnit(
        alpha_2="DZ",
        alpha_3="DZA",
        numeric="012",
        name="Algeria",
        official_name="People's Democratic Republic of Algeria",
    )
    EC = CountryUnit(
        alpha_2="EC",
        alpha_3="ECU",
        numeric="218",
        name="Ecuador",
        official_name="Republic of Ecuador",
    )
    EG = CountryUnit(
        alpha_2="EG",
        alpha_3="EGY",
        numeric="818",
        name="Egypt",
        official_name="Arab Republic of Egypt",
    )
    ER = CountryUnit(
        alpha_2="ER",
        alpha_3="ERI",
        numeric="232",
        name="Eritrea",
        official_name="the State of Eritrea",
    )
    EH = CountryUnit(
        alpha_2="EH",
        alpha_3="ESH",
        numeric="732",
        name="Western Sahara",
        official_name="Western Sahara",
    )
    ES = CountryUnit(
        alpha_2="ES",
        alpha_3="ESP",
        numeric="724",
        name="Spain",
        official_name="Kingdom of Spain",
    )
    EE = CountryUnit(
        alpha_2="EE",
        alpha_3="EST",
        numeric="233",
        name="Estonia",
        official_name="Republic of Estonia",
    )
    ET = CountryUnit(
        alpha_2="ET",
        alpha_3="ETH",
        numeric="231",
        name="Ethiopia",
        official_name="Federal Democratic Republic of Ethiopia",
    )
    FI = CountryUnit(
        alpha_2="FI",
        alpha_3="FIN",
        numeric="246",
        name="Finland",
        official_name="Republic of Finland",
    )
    FJ = CountryUnit(
        alpha_2="FJ",
        alpha_3="FJI",
        numeric="242",
        name="Fiji",
        official_name="Republic of Fiji",
    )
    FK = CountryUnit(
        alpha_2="FK",
        alpha_3="FLK",
        numeric="238",
        name="Falkland Islands (Malvinas)",
        official_name="Falkland Islands (Malvinas)",
    )
    FR = CountryUnit(
        alpha_2="FR",
        alpha_3="FRA",
        numeric="250",
        name="France",
        official_name="French Republic",
    )
    FO = CountryUnit(
        alpha_2="FO",
        alpha_3="FRO",
        numeric="234",
        name="Faroe Islands",
        official_name="Faroe Islands",
    )
    FM = CountryUnit(
        alpha_2="FM",
        alpha_3="FSM",
        numeric="583",
        name="Micronesia, Federated States of",
        official_name="Federated States of Micronesia",
    )
    GA = CountryUnit(
        alpha_2="GA",
        alpha_3="GAB",
        numeric="266",
        name="Gabon",
        official_name="Gabonese Republic",
    )
    GB = CountryUnit(
        alpha_2="GB",
        alpha_3="GBR",
        numeric="826",
        name="United Kingdom",
        official_name="United Kingdom of Great Britain and Northern Ireland",
    )
    GE = CountryUnit(
        alpha_2="GE",
        alpha_3="GEO",
        numeric="268",
        name="Georgia",
        official_name="Georgia",
    )
    GG = CountryUnit(
        alpha_2="GG",
        alpha_3="GGY",
        numeric="831",
        name="Guernsey",
        official_name="Guernsey",
    )
    GH = CountryUnit(
        alpha_2="GH",
        alpha_3="GHA",
        numeric="288",
        name="Ghana",
        official_name="Republic of Ghana",
    )
    GI = CountryUnit(
        alpha_2="GI",
        alpha_3="GIB",
        numeric="292",
        name="Gibraltar",
        official_name="Gibraltar",
    )
    GN = CountryUnit(
        alpha_2="GN",
        alpha_3="GIN",
        numeric="324",
        name="Guinea",
        official_name="Republic of Guinea",
    )
    GP = CountryUnit(
        alpha_2="GP",
        alpha_3="GLP",
        numeric="312",
        name="Guadeloupe",
        official_name="Guadeloupe",
    )
    GM = CountryUnit(
        alpha_2="GM",
        alpha_3="GMB",
        numeric="270",
        name="Gambia",
        official_name="Republic of the Gambia",
    )
    GW = CountryUnit(
        alpha_2="GW",
        alpha_3="GNB",
        numeric="624",
        name="Guinea-Bissau",
        official_name="Republic of Guinea-Bissau",
    )
    GQ = CountryUnit(
        alpha_2="GQ",
        alpha_3="GNQ",
        numeric="226",
        name="Equatorial Guinea",
        official_name="Republic of Equatorial Guinea",
    )
    GR = CountryUnit(
        alpha_2="GR",
        alpha_3="GRC",
        numeric="300",
        name="Greece",
        official_name="Hellenic Republic",
    )
    GD = CountryUnit(
        alpha_2="GD",
        alpha_3="GRD",
        numeric="308",
        name="Grenada",
        official_name="Grenada",
    )
    GL = CountryUnit(
        alpha_2="GL",
        alpha_3="GRL",
        numeric="304",
        name="Greenland",
        official_name="Greenland",
    )
    GT = CountryUnit(
        alpha_2="GT",
        alpha_3="GTM",
        numeric="320",
        name="Guatemala",
        official_name="Republic of Guatemala",
    )
    GF = CountryUnit(
        alpha_2="GF",
        alpha_3="GUF",
        numeric="254",
        name="French Guiana",
        official_name="French Guiana",
    )
    GU = CountryUnit(
        alpha_2="GU",
        alpha_3="GUM",
        numeric="316",
        name="Guam",
        official_name="Guam",
    )
    GY = CountryUnit(
        alpha_2="GY",
        alpha_3="GUY",
        numeric="328",
        name="Guyana",
        official_name="Republic of Guyana",
    )
    HK = CountryUnit(
        alpha_2="HK",
        alpha_3="HKG",
        numeric="344",
        name="Hong Kong",
        official_name="Hong Kong Special Administrative Region of China",
    )
    HM = CountryUnit(
        alpha_2="HM",
        alpha_3="HMD",
        numeric="334",
        name="Heard Island and McDonald Islands",
        official_name="Heard Island and McDonald Islands",
    )
    HN = CountryUnit(
        alpha_2="HN",
        alpha_3="HND",
        numeric="340",
        name="Honduras",
        official_name="Republic of Honduras",
    )
    HR = CountryUnit(
        alpha_2="HR",
        alpha_3="HRV",
        numeric="191",
        name="Croatia",
        official_name="Republic of Croatia",
    )
    HT = CountryUnit(
        alpha_2="HT",
        alpha_3="HTI",
        numeric="332",
        name="Haiti",
        official_name="Republic of Haiti",
    )
    HU = CountryUnit(
        alpha_2="HU",
        alpha_3="HUN",
        numeric="348",
        name="Hungary",
        official_name="Hungary",
    )
    ID = CountryUnit(
        alpha_2="ID",
        alpha_3="IDN",
        numeric="360",
        name="Indonesia",
        official_name="Republic of Indonesia",
    )
    IM = CountryUnit(
        alpha_2="IM",
        alpha_3="IMN",
        numeric="833",
        name="Isle of Man",
        official_name="Isle of Man",
    )
    IN = CountryUnit(
        alpha_2="IN",
        alpha_3="IND",
        numeric="356",
        name="India",
        official_name="Republic of India",
    )
    IO = CountryUnit(
        alpha_2="IO",
        alpha_3="IOT",
        numeric="086",
        name="British Indian Ocean Territory",
        official_name="British Indian Ocean Territory",
    )
    IE = CountryUnit(
        alpha_2="IE",
        alpha_3="IRL",
        numeric="372",
        name="Ireland",
        official_name="Ireland",
    )
    IR = CountryUnit(
        alpha_2="IR",
        alpha_3="IRN",
        numeric="364",
        name="Iran, Islamic Republic of",
        official_name="Islamic Republic of Iran",
    )
    IQ = CountryUnit(
        alpha_2="IQ",
        alpha_3="IRQ",
        numeric="368",
        name="Iraq",
        official_name="Republic of Iraq",
    )
    IS = CountryUnit(
        alpha_2="IS",
        alpha_3="ISL",
        numeric="352",
        name="Iceland",
        official_name="Republic of Iceland",
    )
    IL = CountryUnit(
        alpha_2="IL",
        alpha_3="ISR",
        numeric="376",
        name="Israel",
        official_name="State of Israel",
    )
    IT = CountryUnit(
        alpha_2="IT",
        alpha_3="ITA",
        numeric="380",
        name="Italy",
        official_name="Italian Republic",
    )
    JM = CountryUnit(
        alpha_2="JM",
        alpha_3="JAM",
        numeric="388",
        name="Jamaica",
        official_name="Jamaica",
    )
    JE = CountryUnit(
        alpha_2="JE",
        alpha_3="JEY",
        numeric="832",
        name="Jersey",
        official_name="Jersey",
    )
    JO = CountryUnit(
        alpha_2="JO",
        alpha_3="JOR",
        numeric="400",
        name="Jordan",
        official_name="Hashemite Kingdom of Jordan",
    )
    JP = CountryUnit(
        alpha_2="JP",
        alpha_3="JPN",
        numeric="392",
        name="Japan",
        official_name="Japan",
    )
    KZ = CountryUnit(
        alpha_2="KZ",
        alpha_3="KAZ",
        numeric="398",
        name="Kazakhstan",
        official_name="Republic of Kazakhstan",
    )
    KE = CountryUnit(
        alpha_2="KE",
        alpha_3="KEN",
        numeric="404",
        name="Kenya",
        official_name="Republic of Kenya",
    )
    KG = CountryUnit(
        alpha_2="KG",
        alpha_3="KGZ",
        numeric="417",
        name="Kyrgyzstan",
        official_name="Kyrgyz Republic",
    )
    KH = CountryUnit(
        alpha_2="KH",
        alpha_3="KHM",
        numeric="116",
        name="Cambodia",
        official_name="Kingdom of Cambodia",
    )
    KI = CountryUnit(
        alpha_2="KI",
        alpha_3="KIR",
        numeric="296",
        name="Kiribati",
        official_name="Republic of Kiribati",
    )
    KN = CountryUnit(
        alpha_2="KN",
        alpha_3="KNA",
        numeric="659",
        name="Saint Kitts and Nevis",
        official_name="Saint Kitts and Nevis",
    )
    KR = CountryUnit(
        alpha_2="KR",
        alpha_3="KOR",
        numeric="410",
        name="Korea, Republic of",
        official_name="Korea, Republic of",
    )
    KW = CountryUnit(
        alpha_2="KW",
        alpha_3="KWT",
        numeric="414",
        name="Kuwait",
        official_name="State of Kuwait",
    )
    LA = CountryUnit(
        alpha_2="LA",
        alpha_3="LAO",
        numeric="418",
        name="Lao People's Democratic Republic",
        official_name="Lao People's Democratic Republic",
    )
    LB = CountryUnit(
        alpha_2="LB",
        alpha_3="LBN",
        numeric="422",
        name="Lebanon",
        official_name="Lebanese Republic",
    )
    LR = CountryUnit(
        alpha_2="LR",
        alpha_3="LBR",
        numeric="430",
        name="Liberia",
        official_name="Republic of Liberia",
    )
    LY = CountryUnit(
        alpha_2="LY",
        alpha_3="LBY",
        numeric="434",
        name="Libya",
        official_name="Libya",
    )
    LC = CountryUnit(
        alpha_2="LC",
        alpha_3="LCA",
        numeric="662",
        name="Saint Lucia",
        official_name="Saint Lucia",
    )
    LI = CountryUnit(
        alpha_2="LI",
        alpha_3="LIE",
        numeric="438",
        name="Liechtenstein",
        official_name="Principality of Liechtenstein",
    )
    LK = CountryUnit(
        alpha_2="LK",
        alpha_3="LKA",
        numeric="144",
        name="Sri Lanka",
        official_name="Democratic Socialist Republic of Sri Lanka",
    )
    LS = CountryUnit(
        alpha_2="LS",
        alpha_3="LSO",
        numeric="426",
        name="Lesotho",
        official_name="Kingdom of Lesotho",
    )
    LT = CountryUnit(
        alpha_2="LT",
        alpha_3="LTU",
        numeric="440",
        name="Lithuania",
        official_name="Republic of Lithuania",
    )
    LU = CountryUnit(
        alpha_2="LU",
        alpha_3="LUX",
        numeric="442",
        name="Luxembourg",
        official_name="Grand Duchy of Luxembourg",
    )
    LV = CountryUnit(
        alpha_2="LV",
        alpha_3="LVA",
        numeric="428",
        name="Latvia",
        official_name="Republic of Latvia",
    )
    MO = CountryUnit(
        alpha_2="MO",
        alpha_3="MAC",
        numeric="446",
        name="Macao",
        official_name="Macao Special Administrative Region of China",
    )
    MF = CountryUnit(
        alpha_2="MF",
        alpha_3="MAF",
        numeric="663",
        name="Saint Martin (French part)",
        official_name="Saint Martin (French part)",
    )
    MA = CountryUnit(
        alpha_2="MA",
        alpha_3="MAR",
        numeric="504",
        name="Morocco",
        official_name="Kingdom of Morocco",
    )
    MC = CountryUnit(
        alpha_2="MC",
        alpha_3="MCO",
        numeric="492",
        name="Monaco",
        official_name="Principality of Monaco",
    )
    MD = CountryUnit(
        alpha_2="MD",
        alpha_3="MDA",
        numeric="498",
        name="Moldova, Republic of",
        official_name="Republic of Moldova",
    )
    MG = CountryUnit(
        alpha_2="MG",
        alpha_3="MDG",
        numeric="450",
        name="Madagascar",
        official_name="Republic of Madagascar",
    )
    MV = CountryUnit(
        alpha_2="MV",
        alpha_3="MDV",
        numeric="462",
        name="Maldives",
        official_name="Republic of Maldives",
    )
    MX = CountryUnit(
        alpha_2="MX",
        alpha_3="MEX",
        numeric="484",
        name="Mexico",
        official_name="United Mexican States",
    )
    MH = CountryUnit(
        alpha_2="MH",
        alpha_3="MHL",
        numeric="584",
        name="Marshall Islands",
        official_name="Republic of the Marshall Islands",
    )
    MK = CountryUnit(
        alpha_2="MK",
        alpha_3="MKD",
        numeric="807",
        name="North Macedonia",
        official_name="Republic of North Macedonia",
    )
    ML = CountryUnit(
        alpha_2="ML",
        alpha_3="MLI",
        numeric="466",
        name="Mali",
        official_name="Republic of Mali",
    )
    MT = CountryUnit(
        alpha_2="MT",
        alpha_3="MLT",
        numeric="470",
        name="Malta",
        official_name="Republic of Malta",
    )
    MM = CountryUnit(
        alpha_2="MM",
        alpha_3="MMR",
        numeric="104",
        name="Myanmar",
        official_name="Republic of Myanmar",
    )
    ME = CountryUnit(
        alpha_2="ME",
        alpha_3="MNE",
        numeric="499",
        name="Montenegro",
        official_name="Montenegro",
    )
    MN = CountryUnit(
        alpha_2="MN",
        alpha_3="MNG",
        numeric="496",
        name="Mongolia",
        official_name="Mongolia",
    )
    MP = CountryUnit(
        alpha_2="MP",
        alpha_3="MNP",
        numeric="580",
        name="Northern Mariana Islands",
        official_name="Commonwealth of the Northern Mariana Islands",
    )
    MZ = CountryUnit(
        alpha_2="MZ",
        alpha_3="MOZ",
        numeric="508",
        name="Mozambique",
        official_name="Republic of Mozambique",
    )
    MR = CountryUnit(
        alpha_2="MR",
        alpha_3="MRT",
        numeric="478",
        name="Mauritania",
        official_name="Islamic Republic of Mauritania",
    )
    MS = CountryUnit(
        alpha_2="MS",
        alpha_3="MSR",
        numeric="500",
        name="Montserrat",
        official_name="Montserrat",
    )
    MQ = CountryUnit(
        alpha_2="MQ",
        alpha_3="MTQ",
        numeric="474",
        name="Martinique",
        official_name="Martinique",
    )
    MU = CountryUnit(
        alpha_2="MU",
        alpha_3="MUS",
        numeric="480",
        name="Mauritius",
        official_name="Republic of Mauritius",
    )
    MW = CountryUnit(
        alpha_2="MW",
        alpha_3="MWI",
        numeric="454",
        name="Malawi",
        official_name="Republic of Malawi",
    )
    MY = CountryUnit(
        alpha_2="MY",
        alpha_3="MYS",
        numeric="458",
        name="Malaysia",
        official_name="Malaysia",
    )
    YT = CountryUnit(
        alpha_2="YT",
        alpha_3="MYT",
        numeric="175",
        name="Mayotte",
        official_name="Mayotte",
    )
    NA = CountryUnit(
        alpha_2="NA",
        alpha_3="NAM",
        numeric="516",
        name="Namibia",
        official_name="Republic of Namibia",
    )
    NC = CountryUnit(
        alpha_2="NC",
        alpha_3="NCL",
        numeric="540",
        name="New Caledonia",
        official_name="New Caledonia",
    )
    NE = CountryUnit(
        alpha_2="NE",
        alpha_3="NER",
        numeric="562",
        name="Niger",
        official_name="Republic of the Niger",
    )
    NF = CountryUnit(
        alpha_2="NF",
        alpha_3="NFK",
        numeric="574",
        name="Norfolk Island",
        official_name="Norfolk Island",
    )
    NG = CountryUnit(
        alpha_2="NG",
        alpha_3="NGA",
        numeric="566",
        name="Nigeria",
        official_name="Federal Republic of Nigeria",
    )
    NI = CountryUnit(
        alpha_2="NI",
        alpha_3="NIC",
        numeric="558",
        name="Nicaragua",
        official_name="Republic of Nicaragua",
    )
    NU = CountryUnit(
        alpha_2="NU",
        alpha_3="NIU",
        numeric="570",
        name="Niue",
        official_name="Niue",
    )
    NL = CountryUnit(
        alpha_2="NL",
        alpha_3="NLD",
        numeric="528",
        name="Netherlands",
        official_name="Kingdom of the Netherlands",
    )
    NO = CountryUnit(
        alpha_2="NO",
        alpha_3="NOR",
        numeric="578",
        name="Norway",
        official_name="Kingdom of Norway",
    )
    NP = CountryUnit(
        alpha_2="NP",
        alpha_3="NPL",
        numeric="524",
        name="Nepal",
        official_name="Federal Democratic Republic of Nepal",
    )
    NR = CountryUnit(
        alpha_2="NR",
        alpha_3="NRU",
        numeric="520",
        name="Nauru",
        official_name="Republic of Nauru",
    )
    NZ = CountryUnit(
        alpha_2="NZ",
        alpha_3="NZL",
        numeric="554",
        name="New Zealand",
        official_name="New Zealand",
    )
    OM = CountryUnit(
        alpha_2="OM",
        alpha_3="OMN",
        numeric="512",
        name="Oman",
        official_name="Sultanate of Oman",
    )
    PK = CountryUnit(
        alpha_2="PK",
        alpha_3="PAK",
        numeric="586",
        name="Pakistan",
        official_name="Islamic Republic of Pakistan",
    )
    PA = CountryUnit(
        alpha_2="PA",
        alpha_3="PAN",
        numeric="591",
        name="Panama",
        official_name="Republic of Panama",
    )
    PN = CountryUnit(
        alpha_2="PN",
        alpha_3="PCN",
        numeric="612",
        name="Pitcairn",
        official_name="Pitcairn",
    )
    PE = CountryUnit(
        alpha_2="PE",
        alpha_3="PER",
        numeric="604",
        name="Peru",
        official_name="Republic of Peru",
    )
    PH = CountryUnit(
        alpha_2="PH",
        alpha_3="PHL",
        numeric="608",
        name="Philippines",
        official_name="Republic of the Philippines",
    )
    PW = CountryUnit(
        alpha_2="PW",
        alpha_3="PLW",
        numeric="585",
        name="Palau",
        official_name="Republic of Palau",
    )
    PG = CountryUnit(
        alpha_2="PG",
        alpha_3="PNG",
        numeric="598",
        name="Papua New Guinea",
        official_name="Independent State of Papua New Guinea",
    )
    PL = CountryUnit(
        alpha_2="PL",
        alpha_3="POL",
        numeric="616",
        name="Poland",
        official_name="Republic of Poland",
    )
    PR = CountryUnit(
        alpha_2="PR",
        alpha_3="PRI",
        numeric="630",
        name="Puerto Rico",
        official_name="Puerto Rico",
    )
    KP = CountryUnit(
        alpha_2="KP",
        alpha_3="PRK",
        numeric="408",
        name="Korea, Democratic People's Republic of",
        official_name="Democratic People's Republic of Korea",
    )
    PT = CountryUnit(
        alpha_2="PT",
        alpha_3="PRT",
        numeric="620",
        name="Portugal",
        official_name="Portuguese Republic",
    )
    PY = CountryUnit(
        alpha_2="PY",
        alpha_3="PRY",
        numeric="600",
        name="Paraguay",
        official_name="Republic of Paraguay",
    )
    PS = CountryUnit(
        alpha_2="PS",
        alpha_3="PSE",
        numeric="275",
        name="Palestine, State of",
        official_name="the State of Palestine",
    )
    PF = CountryUnit(
        alpha_2="PF",
        alpha_3="PYF",
        numeric="258",
        name="French Polynesia",
        official_name="French Polynesia",
    )
    QA = CountryUnit(
        alpha_2="QA",
        alpha_3="QAT",
        numeric="634",
        name="Qatar",
        official_name="State of Qatar",
    )
    RE = CountryUnit(
        alpha_2="RE",
        alpha_3="REU",
        numeric="638",
        name="Réunion",
        official_name="Réunion",
    )
    RO = CountryUnit(
        alpha_2="RO",
        alpha_3="ROU",
        numeric="642",
        name="Romania",
        official_name="Romania",
    )
    RU = CountryUnit(
        alpha_2="RU",
        alpha_3="RUS",
        numeric="643",
        name="Russian Federation",
        official_name="Russian Federation",
    )
    RW = CountryUnit(
        alpha_2="RW",
        alpha_3="RWA",
        numeric="646",
        name="Rwanda",
        official_name="Rwandese Republic",
    )
    SA = CountryUnit(
        alpha_2="SA",
        alpha_3="SAU",
        numeric="682",
        name="Saudi Arabia",
        official_name="Kingdom of Saudi Arabia",
    )
    SD = CountryUnit(
        alpha_2="SD",
        alpha_3="SDN",
        numeric="729",
        name="Sudan",
        official_name="Republic of the Sudan",
    )
    SN = CountryUnit(
        alpha_2="SN",
        alpha_3="SEN",
        numeric="686",
        name="Senegal",
        official_name="Republic of Senegal",
    )
    SG = CountryUnit(
        alpha_2="SG",
        alpha_3="SGP",
        numeric="702",
        name="Singapore",
        official_name="Republic of Singapore",
    )
    GS = CountryUnit(
        alpha_2="GS",
        alpha_3="SGS",
        numeric="239",
        name="South Georgia and the South Sandwich Islands",
        official_name="South Georgia and the South Sandwich Islands",
    )
    SH = CountryUnit(
        alpha_2="SH",
        alpha_3="SHN",
        numeric="654",
        name="Saint Helena, Ascension and Tristan da Cunha",
        official_name="Saint Helena, Ascension and Tristan da Cunha",
    )
    SJ = CountryUnit(
        alpha_2="SJ",
        alpha_3="SJM",
        numeric="744",
        name="Svalbard and Jan Mayen",
        official_name="Svalbard and Jan Mayen",
    )
    SB = CountryUnit(
        alpha_2="SB",
        alpha_3="SLB",
        numeric="090",
        name="Solomon Islands",
        official_name="Solomon Islands",
    )
    SL = CountryUnit(
        alpha_2="SL",
        alpha_3="SLE",
        numeric="694",
        name="Sierra Leone",
        official_name="Republic of Sierra Leone",
    )
    SV = CountryUnit(
        alpha_2="SV",
        alpha_3="SLV",
        numeric="222",
        name="El Salvador",
        official_name="Republic of El Salvador",
    )
    SM = CountryUnit(
        alpha_2="SM",
        alpha_3="SMR",
        numeric="674",
        name="San Marino",
        official_name="Republic of San Marino",
    )
    SO = CountryUnit(
        alpha_2="SO",
        alpha_3="SOM",
        numeric="706",
        name="Somalia",
        official_name="Federal Republic of Somalia",
    )
    PM = CountryUnit(
        alpha_2="PM",
        alpha_3="SPM",
        numeric="666",
        name="Saint Pierre and Miquelon",
        official_name="Saint Pierre and Miquelon",
    )
    RS = CountryUnit(
        alpha_2="RS",
        alpha_3="SRB",
        numeric="688",
        name="Serbia",
        official_name="Republic of Serbia",
    )
    SS = CountryUnit(
        alpha_2="SS",
        alpha_3="SSD",
        numeric="728",
        name="South Sudan",
        official_name="Republic of South Sudan",
    )
    ST = CountryUnit(
        alpha_2="ST",
        alpha_3="STP",
        numeric="678",
        name="Sao Tome and Principe",
        official_name="Democratic Republic of Sao Tome and Principe",
    )
    SR = CountryUnit(
        alpha_2="SR",
        alpha_3="SUR",
        numeric="740",
        name="Suriname",
        official_name="Republic of Suriname",
    )
    SK = CountryUnit(
        alpha_2="SK",
        alpha_3="SVK",
        numeric="703",
        name="Slovakia",
        official_name="Slovak Republic",
    )
    SI = CountryUnit(
        alpha_2="SI",
        alpha_3="SVN",
        numeric="705",
        name="Slovenia",
        official_name="Republic of Slovenia",
    )
    SE = CountryUnit(
        alpha_2="SE",
        alpha_3="SWE",
        numeric="752",
        name="Sweden",
        official_name="Kingdom of Sweden",
    )
    SZ = CountryUnit(
        alpha_2="SZ",
        alpha_3="SWZ",
        numeric="748",
        name="Eswatini",
        official_name="Kingdom of Eswatini",
    )
    SX = CountryUnit(
        alpha_2="SX",
        alpha_3="SXM",
        numeric="534",
        name="Sint Maarten (Dutch part)",
        official_name="Sint Maarten (Dutch part)",
    )
    SC = CountryUnit(
        alpha_2="SC",
        alpha_3="SYC",
        numeric="690",
        name="Seychelles",
        official_name="Republic of Seychelles",
    )
    SY = CountryUnit(
        alpha_2="SY",
        alpha_3="SYR",
        numeric="760",
        name="Syrian Arab Republic",
        official_name="Syrian Arab Republic",
    )
    TC = CountryUnit(
        alpha_2="TC",
        alpha_3="TCA",
        numeric="796",
        name="Turks and Caicos Islands",
        official_name="Turks and Caicos Islands",
    )
    TD = CountryUnit(
        alpha_2="TD",
        alpha_3="TCD",
        numeric="148",
        name="Chad",
        official_name="Republic of Chad",
    )
    TG = CountryUnit(
        alpha_2="TG",
        alpha_3="TGO",
        numeric="768",
        name="Togo",
        official_name="Togolese Republic",
    )
    TH = CountryUnit(
        alpha_2="TH",
        alpha_3="THA",
        numeric="764",
        name="Thailand",
        official_name="Kingdom of Thailand",
    )
    TJ = CountryUnit(
        alpha_2="TJ",
        alpha_3="TJK",
        numeric="762",
        name="Tajikistan",
        official_name="Republic of Tajikistan",
    )
    TK = CountryUnit(
        alpha_2="TK",
        alpha_3="TKL",
        numeric="772",
        name="Tokelau",
        official_name="Tokelau",
    )
    TM = CountryUnit(
        alpha_2="TM",
        alpha_3="TKM",
        numeric="795",
        name="Turkmenistan",
        official_name="Turkmenistan",
    )
    TL = CountryUnit(
        alpha_2="TL",
        alpha_3="TLS",
        numeric="626",
        name="Timor-Leste",
        official_name="Democratic Republic of Timor-Leste",
    )
    TO = CountryUnit(
        alpha_2="TO",
        alpha_3="TON",
        numeric="776",
        name="Tonga",
        official_name="Kingdom of Tonga",
    )
    TT = CountryUnit(
        alpha_2="TT",
        alpha_3="TTO",
        numeric="780",
        name="Trinidad and Tobago",
        official_name="Republic of Trinidad and Tobago",
    )
    TN = CountryUnit(
        alpha_2="TN",
        alpha_3="TUN",
        numeric="788",
        name="Tunisia",
        official_name="Republic of Tunisia",
    )
    TR = CountryUnit(
        alpha_2="TR",
        alpha_3="TUR",
        numeric="792",
        name="Türkiye",
        official_name="Republic of Türkiye",
    )
    TV = CountryUnit(
        alpha_2="TV",
        alpha_3="TUV",
        numeric="798",
        name="Tuvalu",
        official_name="Tuvalu",
    )
    TW = CountryUnit(
        alpha_2="TW",
        alpha_3="TWN",
        numeric="158",
        name="Taiwan, Province of China",
        official_name="Taiwan, Province of China",
    )
    TZ = CountryUnit(
        alpha_2="TZ",
        alpha_3="TZA",
        numeric="834",
        name="Tanzania, United Republic of",
        official_name="United Republic of Tanzania",
    )
    UG = CountryUnit(
        alpha_2="UG",
        alpha_3="UGA",
        numeric="800",
        name="Uganda",
        official_name="Republic of Uganda",
    )
    UA = CountryUnit(
        alpha_2="UA",
        alpha_3="UKR",
        numeric="804",
        name="Ukraine",
        official_name="Ukraine",
    )
    UM = CountryUnit(
        alpha_2="UM",
        alpha_3="UMI",
        numeric="581",
        name="United States Minor Outlying Islands",
        official_name="United States Minor Outlying Islands",
    )
    UY = CountryUnit(
        alpha_2="UY",
        alpha_3="URY",
        numeric="858",
        name="Uruguay",
        official_name="Eastern Republic of Uruguay",
    )
    US = CountryUnit(
        alpha_2="US",
        alpha_3="USA",
        numeric="840",
        name="United States",
        official_name="United States of America",
    )
    UZ = CountryUnit(
        alpha_2="UZ",
        alpha_3="UZB",
        numeric="860",
        name="Uzbekistan",
        official_name="Republic of Uzbekistan",
    )
    VA = CountryUnit(
        alpha_2="VA",
        alpha_3="VAT",
        numeric="336",
        name="Holy See (Vatican City State)",
        official_name="Holy See (Vatican City State)",
    )
    VC = CountryUnit(
        alpha_2="VC",
        alpha_3="VCT",
        numeric="670",
        name="Saint Vincent and the Grenadines",
        official_name="Saint Vincent and the Grenadines",
    )
    VE = CountryUnit(
        alpha_2="VE",
        alpha_3="VEN",
        numeric="862",
        name="Venezuela, Bolivarian Republic of",
        official_name="Bolivarian Republic of Venezuela",
    )
    VG = CountryUnit(
        alpha_2="VG",
        alpha_3="VGB",
        numeric="092",
        name="Virgin Islands, British",
        official_name="British Virgin Islands",
    )
    VI = CountryUnit(
        alpha_2="VI",
        alpha_3="VIR",
        numeric="850",
        name="Virgin Islands, U.S.",
        official_name="Virgin Islands of the United States",
    )
    VN = CountryUnit(
        alpha_2="VN",
        alpha_3="VNM",
        numeric="704",
        name="Viet Nam",
        official_name="Socialist Republic of Viet Nam",
    )
    VU = CountryUnit(
        alpha_2="VU",
        alpha_3="VUT",
        numeric="548",
        name="Vanuatu",
        official_name="Republic of Vanuatu",
    )
    WF = CountryUnit(
        alpha_2="WF",
        alpha_3="WLF",
        numeric="876",
        name="Wallis and Futuna",
        official_name="Wallis and Futuna",
    )
    WS = CountryUnit(
        alpha_2="WS",
        alpha_3="WSM",
        numeric="882",
        name="Samoa",
        official_name="Independent State of Samoa",
    )
    YE = CountryUnit(
        alpha_2="YE",
        alpha_3="YEM",
        numeric="887",
        name="Yemen",
        official_name="Republic of Yemen",
    )
    ZA = CountryUnit(
        alpha_2="ZA",
        alpha_3="ZAF",
        numeric="710",
        name="South Africa",
        official_name="Republic of South Africa",
    )
    ZM = CountryUnit(
        alpha_2="ZM",
        alpha_3="ZMB",
        numeric="894",
        name="Zambia",
        official_name="Republic of Zambia",
    )
    ZW = CountryUnit(
        alpha_2="ZW",
        alpha_3="ZWE",
        numeric="716",
        name="Zimbabwe",
        official_name="Republic of Zimbabwe",
    )

    @property
    def unit(self) -> CountryUnit:
        """
        Returns:
            ``pycountries.countries.CountryUnit``.
        """
        return self._value_

    @property
    def value(self):
        """
        Returns:
            ISO 3166-1 Alpha 2 code.
        """
        return self.unit.alpha_2

    @property
    def alpha_2(self) -> str:
        """
        This code is used as part of domain names, vehicle registration plates, and in international
        transactions, among other purposes.

        Returns:
            ISO 3166-1 Alpha 2 code.
        """
        return self.unit.alpha_2

    @property
    def alpha_3(self) -> str:
        """
        This code is commonly used in various international contexts,
        including identifying countries in internet domains, representing countries in airline
        ticketing, and facilitating international trade.

        Returns:
            ISO 3166-1 Alpha 3 code.
        """
        return self.unit.alpha_3

    @property
    def numeric(self):
        """
        This code is used in various contexts where numeric representations are preferred over
        alphanumeric ones, such as in databases or systems where numerical identifiers are
        easier to work with.

        Returns:
            ISO 3166-1 numeric code.
        """
        return self.unit.numeric

    @property
    def name(self) -> str:
        """
        Unofficial country name, known as shorten country name.

        Returns:
            ISO 3166 name.
        """
        return self.unit.name

    @property
    def official_name(self) -> str:
        """
        Official country name.

        Returns:
            World Factbook official state name.
        """
        return self.unit.official_name

    def __str__(self) -> str:
        return self.value
