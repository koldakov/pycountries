from __future__ import annotations

import sys
from enum import Enum

from pydantic import BaseModel, Field

from pycountries._base import EnumTypeBase


class LanguageUnitBase(BaseModel):
    name: str = Field(
        description="Official Language name.",
        examples=[
            "English",
            "French",
            "Russian",
        ],
    )
    alpha_3: str = Field(
        min_length=3,
        max_length=3,
        description="ISO 639-2 three-letter code to represent language.",
        examples=[
            "eng",
            "fra",
            "rus",
        ],
    )
    terminology: str = Field(
        min_length=3,
        max_length=3,
        description="ISO 639-2 code refers to specific language code designated for terminology or "
        "specialized vocabulary purposes.",
        examples=[
            "eng",
            "fra",
            "rus",
        ],
    )


if sys.version_info >= (3, 10):  # noqa: UP036

    class LanguageUnit(LanguageUnitBase):
        alpha_2: str | None = Field(
            default=None,
            min_length=2,
            max_length=2,
            description="ISO 639-2 two-letter code to represent language.",
            examples=[
                "en",
                "ru",
            ],
        )
        bibliographic: str | None = Field(
            min_length=3,
            max_length=3,
            description="ISO 639-2 code designated specifically for bibliographic or library cataloging purposes. "
            "Bibliographic code is used primarily in library systems and databases to categorize and "
            "organize resources by language.",
            examples=[
                None,
                "fre",
                None,
            ],
        )
else:
    from typing import Optional

    class LanguageUnit(LanguageUnitBase):
        alpha_2: Optional[str] = Field(  # noqa: UP007
            default=None,
            min_length=2,
            max_length=2,
            description="ISO 639-2 two-letter code to represent language.",
            examples=[
                "en",
                "ru",
            ],
        )
        bibliographic: Optional[str] = Field(  # noqa: UP007
            min_length=3,
            max_length=3,
            description="ISO 639-2 code designated specifically for bibliographic or library cataloging purposes. "
            "Bibliographic code is used primarily in library systems and databases to categorize and "
            "organize resources by language.",
            examples=[
                None,
                "fre",
                None,
            ],
        )


def _get_compare_list(language: Language) -> list[str]:
    compare_list: list[str] = [
        language.alpha_3,
    ]
    if language.alpha_2 is not None:
        compare_list.append(language.alpha_2)

    return compare_list


class _LanguageEnumType(EnumTypeBase):
    def __call__(cls, value, *args, **kw):  # noqa: N805
        _members = cls.__members__.values()  # type: ignore[var-annotated]
        language: Language
        for language in _members:
            if value in _get_compare_list(language):
                return language
        raise ValueError(f'"{value}" is not a valid {cls.__qualname__}') from None


class Language(Enum, metaclass=_LanguageEnumType):
    """
    The Language Enum comprises the ISO 639 standard, encompassing both the two-letter Alpha-2 codes and
    the three-letter Alpha-3 codes. Additionally, certain languages may have alternative codes designated for
    bibliographic or terminology purposes.
    """

    AAR = LanguageUnit(
        name="Afar",
        alpha_2="aa",
        alpha_3="aar",
        bibliographic=None,
        terminology="aar",
    )
    ABK = LanguageUnit(
        name="Abkhazian",
        alpha_2="ab",
        alpha_3="abk",
        bibliographic=None,
        terminology="abk",
    )
    ACE = LanguageUnit(
        name="Achinese",
        alpha_2=None,
        alpha_3="ace",
        bibliographic=None,
        terminology="ace",
    )
    ACH = LanguageUnit(
        name="Acoli",
        alpha_2=None,
        alpha_3="ach",
        bibliographic=None,
        terminology="ach",
    )
    ADA = LanguageUnit(
        name="Adangme",
        alpha_2=None,
        alpha_3="ada",
        bibliographic=None,
        terminology="ada",
    )
    ADY = LanguageUnit(
        name="Adyghe; Adygei",
        alpha_2=None,
        alpha_3="ady",
        bibliographic=None,
        terminology="ady",
    )
    AFA = LanguageUnit(
        name="Afro-Asiatic languages",
        alpha_2=None,
        alpha_3="afa",
        bibliographic=None,
        terminology="afa",
    )
    AFH = LanguageUnit(
        name="Afrihili",
        alpha_2=None,
        alpha_3="afh",
        bibliographic=None,
        terminology="afh",
    )
    AFR = LanguageUnit(
        name="Afrikaans",
        alpha_2="af",
        alpha_3="afr",
        bibliographic=None,
        terminology="afr",
    )
    AIN = LanguageUnit(
        name="Ainu",
        alpha_2=None,
        alpha_3="ain",
        bibliographic=None,
        terminology="ain",
    )
    AKA = LanguageUnit(
        name="Akan",
        alpha_2="ak",
        alpha_3="aka",
        bibliographic=None,
        terminology="aka",
    )
    AKK = LanguageUnit(
        name="Akkadian",
        alpha_2=None,
        alpha_3="akk",
        bibliographic=None,
        terminology="akk",
    )
    ALB = LanguageUnit(
        name="Albanian",
        alpha_2="sq",
        alpha_3="alb",
        bibliographic="alb",
        terminology="sqi",
    )
    SQI = LanguageUnit(
        name="Albanian",
        alpha_2="sq",
        alpha_3="sqi",
        bibliographic="alb",
        terminology="sqi",
    )
    ALE = LanguageUnit(
        name="Aleut",
        alpha_2=None,
        alpha_3="ale",
        bibliographic=None,
        terminology="ale",
    )
    ALG = LanguageUnit(
        name="Algonquian languages",
        alpha_2=None,
        alpha_3="alg",
        bibliographic=None,
        terminology="alg",
    )
    ALT = LanguageUnit(
        name="Southern Altai",
        alpha_2=None,
        alpha_3="alt",
        bibliographic=None,
        terminology="alt",
    )
    AMH = LanguageUnit(
        name="Amharic",
        alpha_2="am",
        alpha_3="amh",
        bibliographic=None,
        terminology="amh",
    )
    ANG = LanguageUnit(
        name="English, Old (ca.450-1100)",
        alpha_2=None,
        alpha_3="ang",
        bibliographic=None,
        terminology="ang",
    )
    ANP = LanguageUnit(
        name="Angika",
        alpha_2=None,
        alpha_3="anp",
        bibliographic=None,
        terminology="anp",
    )
    APA = LanguageUnit(
        name="Apache languages",
        alpha_2=None,
        alpha_3="apa",
        bibliographic=None,
        terminology="apa",
    )
    ARA = LanguageUnit(
        name="Arabic",
        alpha_2="ar",
        alpha_3="ara",
        bibliographic=None,
        terminology="ara",
    )
    ARC = LanguageUnit(
        name="Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)",
        alpha_2=None,
        alpha_3="arc",
        bibliographic=None,
        terminology="arc",
    )
    ARG = LanguageUnit(
        name="Aragonese",
        alpha_2="an",
        alpha_3="arg",
        bibliographic=None,
        terminology="arg",
    )
    ARM = LanguageUnit(
        name="Armenian",
        alpha_2="hy",
        alpha_3="arm",
        bibliographic="arm",
        terminology="hye",
    )
    HYE = LanguageUnit(
        name="Armenian",
        alpha_2="hy",
        alpha_3="hye",
        bibliographic="arm",
        terminology="hye",
    )
    ARN = LanguageUnit(
        name="Mapudungun; Mapuche",
        alpha_2=None,
        alpha_3="arn",
        bibliographic=None,
        terminology="arn",
    )
    ARP = LanguageUnit(
        name="Arapaho",
        alpha_2=None,
        alpha_3="arp",
        bibliographic=None,
        terminology="arp",
    )
    ART = LanguageUnit(
        name="Artificial languages",
        alpha_2=None,
        alpha_3="art",
        bibliographic=None,
        terminology="art",
    )
    ARW = LanguageUnit(
        name="Arawak",
        alpha_2=None,
        alpha_3="arw",
        bibliographic=None,
        terminology="arw",
    )
    ASM = LanguageUnit(
        name="Assamese",
        alpha_2="as",
        alpha_3="asm",
        bibliographic=None,
        terminology="asm",
    )
    AST = LanguageUnit(
        name="Asturian; Bable; Leonese; Asturleonese",
        alpha_2=None,
        alpha_3="ast",
        bibliographic=None,
        terminology="ast",
    )
    ATH = LanguageUnit(
        name="Athapascan languages",
        alpha_2=None,
        alpha_3="ath",
        bibliographic=None,
        terminology="ath",
    )
    AUS = LanguageUnit(
        name="Australian languages",
        alpha_2=None,
        alpha_3="aus",
        bibliographic=None,
        terminology="aus",
    )
    AVA = LanguageUnit(
        name="Avaric",
        alpha_2="av",
        alpha_3="ava",
        bibliographic=None,
        terminology="ava",
    )
    AVE = LanguageUnit(
        name="Avestan",
        alpha_2="ae",
        alpha_3="ave",
        bibliographic=None,
        terminology="ave",
    )
    AWA = LanguageUnit(
        name="Awadhi",
        alpha_2=None,
        alpha_3="awa",
        bibliographic=None,
        terminology="awa",
    )
    AYM = LanguageUnit(
        name="Aymara",
        alpha_2="ay",
        alpha_3="aym",
        bibliographic=None,
        terminology="aym",
    )
    AZE = LanguageUnit(
        name="Azerbaijani",
        alpha_2="az",
        alpha_3="aze",
        bibliographic=None,
        terminology="aze",
    )
    BAD = LanguageUnit(
        name="Banda languages",
        alpha_2=None,
        alpha_3="bad",
        bibliographic=None,
        terminology="bad",
    )
    BAI = LanguageUnit(
        name="Bamileke languages",
        alpha_2=None,
        alpha_3="bai",
        bibliographic=None,
        terminology="bai",
    )
    BAK = LanguageUnit(
        name="Bashkir",
        alpha_2="ba",
        alpha_3="bak",
        bibliographic=None,
        terminology="bak",
    )
    BAL = LanguageUnit(
        name="Baluchi",
        alpha_2=None,
        alpha_3="bal",
        bibliographic=None,
        terminology="bal",
    )
    BAM = LanguageUnit(
        name="Bambara",
        alpha_2="bm",
        alpha_3="bam",
        bibliographic=None,
        terminology="bam",
    )
    BAN = LanguageUnit(
        name="Balinese",
        alpha_2=None,
        alpha_3="ban",
        bibliographic=None,
        terminology="ban",
    )
    BAQ = LanguageUnit(
        name="Basque",
        alpha_2="eu",
        alpha_3="baq",
        bibliographic="baq",
        terminology="eus",
    )
    EUS = LanguageUnit(
        name="Basque",
        alpha_2="eu",
        alpha_3="eus",
        bibliographic="baq",
        terminology="eus",
    )
    BAS = LanguageUnit(
        name="Basa",
        alpha_2=None,
        alpha_3="bas",
        bibliographic=None,
        terminology="bas",
    )
    BAT = LanguageUnit(
        name="Baltic languages",
        alpha_2=None,
        alpha_3="bat",
        bibliographic=None,
        terminology="bat",
    )
    BEJ = LanguageUnit(
        name="Beja; Bedawiyet",
        alpha_2=None,
        alpha_3="bej",
        bibliographic=None,
        terminology="bej",
    )
    BEL = LanguageUnit(
        name="Belarusian",
        alpha_2="be",
        alpha_3="bel",
        bibliographic=None,
        terminology="bel",
    )
    BEM = LanguageUnit(
        name="Bemba",
        alpha_2=None,
        alpha_3="bem",
        bibliographic=None,
        terminology="bem",
    )
    BEN = LanguageUnit(
        name="Bengali",
        alpha_2="bn",
        alpha_3="ben",
        bibliographic=None,
        terminology="ben",
    )
    BER = LanguageUnit(
        name="Berber languages",
        alpha_2=None,
        alpha_3="ber",
        bibliographic=None,
        terminology="ber",
    )
    BHO = LanguageUnit(
        name="Bhojpuri",
        alpha_2=None,
        alpha_3="bho",
        bibliographic=None,
        terminology="bho",
    )
    BIH = LanguageUnit(
        name="Bihari languages",
        alpha_2="bh",
        alpha_3="bih",
        bibliographic=None,
        terminology="bih",
    )
    BIK = LanguageUnit(
        name="Bikol",
        alpha_2=None,
        alpha_3="bik",
        bibliographic=None,
        terminology="bik",
    )
    BIN = LanguageUnit(
        name="Bini; Edo",
        alpha_2=None,
        alpha_3="bin",
        bibliographic=None,
        terminology="bin",
    )
    BIS = LanguageUnit(
        name="Bislama",
        alpha_2="bi",
        alpha_3="bis",
        bibliographic=None,
        terminology="bis",
    )
    BLA = LanguageUnit(
        name="Siksika",
        alpha_2=None,
        alpha_3="bla",
        bibliographic=None,
        terminology="bla",
    )
    BNT = LanguageUnit(
        name="Bantu languages",
        alpha_2=None,
        alpha_3="bnt",
        bibliographic=None,
        terminology="bnt",
    )
    TIB = LanguageUnit(
        name="Tibetan",
        alpha_2="bo",
        alpha_3="tib",
        bibliographic="tib",
        terminology="bod",
    )
    BOD = LanguageUnit(
        name="Tibetan",
        alpha_2="bo",
        alpha_3="bod",
        bibliographic="tib",
        terminology="bod",
    )
    BOS = LanguageUnit(
        name="Bosnian",
        alpha_2="bs",
        alpha_3="bos",
        bibliographic=None,
        terminology="bos",
    )
    BRA = LanguageUnit(
        name="Braj",
        alpha_2=None,
        alpha_3="bra",
        bibliographic=None,
        terminology="bra",
    )
    BRE = LanguageUnit(
        name="Breton",
        alpha_2="br",
        alpha_3="bre",
        bibliographic=None,
        terminology="bre",
    )
    BTK = LanguageUnit(
        name="Batak languages",
        alpha_2=None,
        alpha_3="btk",
        bibliographic=None,
        terminology="btk",
    )
    BUA = LanguageUnit(
        name="Buriat",
        alpha_2=None,
        alpha_3="bua",
        bibliographic=None,
        terminology="bua",
    )
    BUG = LanguageUnit(
        name="Buginese",
        alpha_2=None,
        alpha_3="bug",
        bibliographic=None,
        terminology="bug",
    )
    BUL = LanguageUnit(
        name="Bulgarian",
        alpha_2="bg",
        alpha_3="bul",
        bibliographic=None,
        terminology="bul",
    )
    BUR = LanguageUnit(
        name="Burmese",
        alpha_2="my",
        alpha_3="bur",
        bibliographic="bur",
        terminology="mya",
    )
    MYA = LanguageUnit(
        name="Burmese",
        alpha_2="my",
        alpha_3="mya",
        bibliographic="bur",
        terminology="mya",
    )
    BYN = LanguageUnit(
        name="Blin; Bilin",
        alpha_2=None,
        alpha_3="byn",
        bibliographic=None,
        terminology="byn",
    )
    CAD = LanguageUnit(
        name="Caddo",
        alpha_2=None,
        alpha_3="cad",
        bibliographic=None,
        terminology="cad",
    )
    CAI = LanguageUnit(
        name="Central American Indian languages",
        alpha_2=None,
        alpha_3="cai",
        bibliographic=None,
        terminology="cai",
    )
    CAR = LanguageUnit(
        name="Galibi Carib",
        alpha_2=None,
        alpha_3="car",
        bibliographic=None,
        terminology="car",
    )
    CAT = LanguageUnit(
        name="Catalan; Valencian",
        alpha_2="ca",
        alpha_3="cat",
        bibliographic=None,
        terminology="cat",
    )
    CAU = LanguageUnit(
        name="Caucasian languages",
        alpha_2=None,
        alpha_3="cau",
        bibliographic=None,
        terminology="cau",
    )
    CEB = LanguageUnit(
        name="Cebuano",
        alpha_2=None,
        alpha_3="ceb",
        bibliographic=None,
        terminology="ceb",
    )
    CEL = LanguageUnit(
        name="Celtic languages",
        alpha_2=None,
        alpha_3="cel",
        bibliographic=None,
        terminology="cel",
    )
    CZE = LanguageUnit(
        name="Czech",
        alpha_2="cs",
        alpha_3="cze",
        bibliographic="cze",
        terminology="ces",
    )
    CES = LanguageUnit(
        name="Czech",
        alpha_2="cs",
        alpha_3="ces",
        bibliographic="cze",
        terminology="ces",
    )
    CHA = LanguageUnit(
        name="Chamorro",
        alpha_2="ch",
        alpha_3="cha",
        bibliographic=None,
        terminology="cha",
    )
    CHB = LanguageUnit(
        name="Chibcha",
        alpha_2=None,
        alpha_3="chb",
        bibliographic=None,
        terminology="chb",
    )
    CHE = LanguageUnit(
        name="Chechen",
        alpha_2="ce",
        alpha_3="che",
        bibliographic=None,
        terminology="che",
    )
    CHG = LanguageUnit(
        name="Chagatai",
        alpha_2=None,
        alpha_3="chg",
        bibliographic=None,
        terminology="chg",
    )
    CHI = LanguageUnit(
        name="Chinese",
        alpha_2="zh",
        alpha_3="chi",
        bibliographic="chi",
        terminology="zho",
    )
    ZHO = LanguageUnit(
        name="Chinese",
        alpha_2="zh",
        alpha_3="zho",
        bibliographic="chi",
        terminology="zho",
    )
    CHK = LanguageUnit(
        name="Chuukese",
        alpha_2=None,
        alpha_3="chk",
        bibliographic=None,
        terminology="chk",
    )
    CHM = LanguageUnit(
        name="Mari",
        alpha_2=None,
        alpha_3="chm",
        bibliographic=None,
        terminology="chm",
    )
    CHN = LanguageUnit(
        name="Chinook jargon",
        alpha_2=None,
        alpha_3="chn",
        bibliographic=None,
        terminology="chn",
    )
    CHO = LanguageUnit(
        name="Choctaw",
        alpha_2=None,
        alpha_3="cho",
        bibliographic=None,
        terminology="cho",
    )
    CHP = LanguageUnit(
        name="Chipewyan; Dene Suline",
        alpha_2=None,
        alpha_3="chp",
        bibliographic=None,
        terminology="chp",
    )
    CHR = LanguageUnit(
        name="Cherokee",
        alpha_2=None,
        alpha_3="chr",
        bibliographic=None,
        terminology="chr",
    )
    CHU = LanguageUnit(
        name="Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic",
        alpha_2="cu",
        alpha_3="chu",
        bibliographic=None,
        terminology="chu",
    )
    CHV = LanguageUnit(
        name="Chuvash",
        alpha_2="cv",
        alpha_3="chv",
        bibliographic=None,
        terminology="chv",
    )
    CHY = LanguageUnit(
        name="Cheyenne",
        alpha_2=None,
        alpha_3="chy",
        bibliographic=None,
        terminology="chy",
    )
    CMC = LanguageUnit(
        name="Chamic languages",
        alpha_2=None,
        alpha_3="cmc",
        bibliographic=None,
        terminology="cmc",
    )
    CNR = LanguageUnit(
        name="Montenegrin",
        alpha_2=None,
        alpha_3="cnr",
        bibliographic=None,
        terminology="cnr",
    )
    COP = LanguageUnit(
        name="Coptic",
        alpha_2=None,
        alpha_3="cop",
        bibliographic=None,
        terminology="cop",
    )
    COR = LanguageUnit(
        name="Cornish",
        alpha_2="kw",
        alpha_3="cor",
        bibliographic=None,
        terminology="cor",
    )
    COS = LanguageUnit(
        name="Corsican",
        alpha_2="co",
        alpha_3="cos",
        bibliographic=None,
        terminology="cos",
    )
    CPE = LanguageUnit(
        name="Creoles and pidgins, English based",
        alpha_2=None,
        alpha_3="cpe",
        bibliographic=None,
        terminology="cpe",
    )
    CPF = LanguageUnit(
        name="Creoles and pidgins, French-based",
        alpha_2=None,
        alpha_3="cpf",
        bibliographic=None,
        terminology="cpf",
    )
    CPP = LanguageUnit(
        name="Creoles and pidgins, Portuguese-based",
        alpha_2=None,
        alpha_3="cpp",
        bibliographic=None,
        terminology="cpp",
    )
    CRE = LanguageUnit(
        name="Cree",
        alpha_2="cr",
        alpha_3="cre",
        bibliographic=None,
        terminology="cre",
    )
    CRH = LanguageUnit(
        name="Crimean Tatar; Crimean Turkish",
        alpha_2=None,
        alpha_3="crh",
        bibliographic=None,
        terminology="crh",
    )
    CRP = LanguageUnit(
        name="Creoles and pidgins",
        alpha_2=None,
        alpha_3="crp",
        bibliographic=None,
        terminology="crp",
    )
    CSB = LanguageUnit(
        name="Kashubian",
        alpha_2=None,
        alpha_3="csb",
        bibliographic=None,
        terminology="csb",
    )
    CUS = LanguageUnit(
        name="Cushitic languages",
        alpha_2=None,
        alpha_3="cus",
        bibliographic=None,
        terminology="cus",
    )
    WEL = LanguageUnit(
        name="Welsh",
        alpha_2="cy",
        alpha_3="wel",
        bibliographic="wel",
        terminology="cym",
    )
    CYM = LanguageUnit(
        name="Welsh",
        alpha_2="cy",
        alpha_3="cym",
        bibliographic="wel",
        terminology="cym",
    )
    DAK = LanguageUnit(
        name="Dakota",
        alpha_2=None,
        alpha_3="dak",
        bibliographic=None,
        terminology="dak",
    )
    DAN = LanguageUnit(
        name="Danish",
        alpha_2="da",
        alpha_3="dan",
        bibliographic=None,
        terminology="dan",
    )
    DAR = LanguageUnit(
        name="Dargwa",
        alpha_2=None,
        alpha_3="dar",
        bibliographic=None,
        terminology="dar",
    )
    DAY = LanguageUnit(
        name="Land Dayak languages",
        alpha_2=None,
        alpha_3="day",
        bibliographic=None,
        terminology="day",
    )
    DEL = LanguageUnit(
        name="Delaware",
        alpha_2=None,
        alpha_3="del",
        bibliographic=None,
        terminology="del",
    )
    DEN = LanguageUnit(
        name="Slave (Athapascan)",
        alpha_2=None,
        alpha_3="den",
        bibliographic=None,
        terminology="den",
    )
    GER = LanguageUnit(
        name="German",
        alpha_2="de",
        alpha_3="ger",
        bibliographic="ger",
        terminology="deu",
    )
    DEU = LanguageUnit(
        name="German",
        alpha_2="de",
        alpha_3="deu",
        bibliographic="ger",
        terminology="deu",
    )
    DGR = LanguageUnit(
        name="Dogrib",
        alpha_2=None,
        alpha_3="dgr",
        bibliographic=None,
        terminology="dgr",
    )
    DIN = LanguageUnit(
        name="Dinka",
        alpha_2=None,
        alpha_3="din",
        bibliographic=None,
        terminology="din",
    )
    DIV = LanguageUnit(
        name="Divehi; Dhivehi; Maldivian",
        alpha_2="dv",
        alpha_3="div",
        bibliographic=None,
        terminology="div",
    )
    DOI = LanguageUnit(
        name="Dogri",
        alpha_2=None,
        alpha_3="doi",
        bibliographic=None,
        terminology="doi",
    )
    DRA = LanguageUnit(
        name="Dravidian languages",
        alpha_2=None,
        alpha_3="dra",
        bibliographic=None,
        terminology="dra",
    )
    DSB = LanguageUnit(
        name="Lower Sorbian",
        alpha_2=None,
        alpha_3="dsb",
        bibliographic=None,
        terminology="dsb",
    )
    DUA = LanguageUnit(
        name="Duala",
        alpha_2=None,
        alpha_3="dua",
        bibliographic=None,
        terminology="dua",
    )
    DUM = LanguageUnit(
        name="Dutch, Middle (ca.1050-1350)",
        alpha_2=None,
        alpha_3="dum",
        bibliographic=None,
        terminology="dum",
    )
    DUT = LanguageUnit(
        name="Dutch; Flemish",
        alpha_2="nl",
        alpha_3="dut",
        bibliographic="dut",
        terminology="nld",
    )
    NLD = LanguageUnit(
        name="Dutch; Flemish",
        alpha_2="nl",
        alpha_3="nld",
        bibliographic="dut",
        terminology="nld",
    )
    DYU = LanguageUnit(
        name="Dyula",
        alpha_2=None,
        alpha_3="dyu",
        bibliographic=None,
        terminology="dyu",
    )
    DZO = LanguageUnit(
        name="Dzongkha",
        alpha_2="dz",
        alpha_3="dzo",
        bibliographic=None,
        terminology="dzo",
    )
    EFI = LanguageUnit(
        name="Efik",
        alpha_2=None,
        alpha_3="efi",
        bibliographic=None,
        terminology="efi",
    )
    EGY = LanguageUnit(
        name="Egyptian (Ancient)",
        alpha_2=None,
        alpha_3="egy",
        bibliographic=None,
        terminology="egy",
    )
    EKA = LanguageUnit(
        name="Ekajuk",
        alpha_2=None,
        alpha_3="eka",
        bibliographic=None,
        terminology="eka",
    )
    GRE = LanguageUnit(
        name="Greek, Modern (1453-)",
        alpha_2="el",
        alpha_3="gre",
        bibliographic="gre",
        terminology="ell",
    )
    ELL = LanguageUnit(
        name="Greek, Modern (1453-)",
        alpha_2="el",
        alpha_3="ell",
        bibliographic="gre",
        terminology="ell",
    )
    ELX = LanguageUnit(
        name="Elamite",
        alpha_2=None,
        alpha_3="elx",
        bibliographic=None,
        terminology="elx",
    )
    ENG = LanguageUnit(
        name="English",
        alpha_2="en",
        alpha_3="eng",
        bibliographic=None,
        terminology="eng",
    )
    ENM = LanguageUnit(
        name="English, Middle (1100-1500)",
        alpha_2=None,
        alpha_3="enm",
        bibliographic=None,
        terminology="enm",
    )
    EPO = LanguageUnit(
        name="Esperanto",
        alpha_2="eo",
        alpha_3="epo",
        bibliographic=None,
        terminology="epo",
    )
    EST = LanguageUnit(
        name="Estonian",
        alpha_2="et",
        alpha_3="est",
        bibliographic=None,
        terminology="est",
    )
    EWE = LanguageUnit(
        name="Ewe",
        alpha_2="ee",
        alpha_3="ewe",
        bibliographic=None,
        terminology="ewe",
    )
    EWO = LanguageUnit(
        name="Ewondo",
        alpha_2=None,
        alpha_3="ewo",
        bibliographic=None,
        terminology="ewo",
    )
    FAN = LanguageUnit(
        name="Fang",
        alpha_2=None,
        alpha_3="fan",
        bibliographic=None,
        terminology="fan",
    )
    FAO = LanguageUnit(
        name="Faroese",
        alpha_2="fo",
        alpha_3="fao",
        bibliographic=None,
        terminology="fao",
    )
    PER = LanguageUnit(
        name="Persian",
        alpha_2="fa",
        alpha_3="per",
        bibliographic="per",
        terminology="fas",
    )
    FAS = LanguageUnit(
        name="Persian",
        alpha_2="fa",
        alpha_3="fas",
        bibliographic="per",
        terminology="fas",
    )
    FAT = LanguageUnit(
        name="Fanti",
        alpha_2=None,
        alpha_3="fat",
        bibliographic=None,
        terminology="fat",
    )
    FIJ = LanguageUnit(
        name="Fijian",
        alpha_2="fj",
        alpha_3="fij",
        bibliographic=None,
        terminology="fij",
    )
    FIL = LanguageUnit(
        name="Filipino; Pilipino",
        alpha_2=None,
        alpha_3="fil",
        bibliographic=None,
        terminology="fil",
    )
    FIN = LanguageUnit(
        name="Finnish",
        alpha_2="fi",
        alpha_3="fin",
        bibliographic=None,
        terminology="fin",
    )
    FIU = LanguageUnit(
        name="Finno-Ugrian languages",
        alpha_2=None,
        alpha_3="fiu",
        bibliographic=None,
        terminology="fiu",
    )
    FON = LanguageUnit(
        name="Fon",
        alpha_2=None,
        alpha_3="fon",
        bibliographic=None,
        terminology="fon",
    )
    FRE = LanguageUnit(
        name="French",
        alpha_2="fr",
        alpha_3="fre",
        bibliographic="fre",
        terminology="fra",
    )
    FRA = LanguageUnit(
        name="French",
        alpha_2="fr",
        alpha_3="fra",
        bibliographic="fre",
        terminology="fra",
    )
    FRM = LanguageUnit(
        name="French, Middle (ca.1400-1600)",
        alpha_2=None,
        alpha_3="frm",
        bibliographic=None,
        terminology="frm",
    )
    FRO = LanguageUnit(
        name="French, Old (842-ca.1400)",
        alpha_2=None,
        alpha_3="fro",
        bibliographic=None,
        terminology="fro",
    )
    FRR = LanguageUnit(
        name="Northern Frisian",
        alpha_2=None,
        alpha_3="frr",
        bibliographic=None,
        terminology="frr",
    )
    FRS = LanguageUnit(
        name="Eastern Frisian",
        alpha_2=None,
        alpha_3="frs",
        bibliographic=None,
        terminology="frs",
    )
    FRY = LanguageUnit(
        name="Western Frisian",
        alpha_2="fy",
        alpha_3="fry",
        bibliographic=None,
        terminology="fry",
    )
    FUL = LanguageUnit(
        name="Fulah",
        alpha_2="ff",
        alpha_3="ful",
        bibliographic=None,
        terminology="ful",
    )
    FUR = LanguageUnit(
        name="Friulian",
        alpha_2=None,
        alpha_3="fur",
        bibliographic=None,
        terminology="fur",
    )
    GAA = LanguageUnit(
        name="Ga",
        alpha_2=None,
        alpha_3="gaa",
        bibliographic=None,
        terminology="gaa",
    )
    GAY = LanguageUnit(
        name="Gayo",
        alpha_2=None,
        alpha_3="gay",
        bibliographic=None,
        terminology="gay",
    )
    GBA = LanguageUnit(
        name="Gbaya",
        alpha_2=None,
        alpha_3="gba",
        bibliographic=None,
        terminology="gba",
    )
    GEM = LanguageUnit(
        name="Germanic languages",
        alpha_2=None,
        alpha_3="gem",
        bibliographic=None,
        terminology="gem",
    )
    GEO = LanguageUnit(
        name="Georgian",
        alpha_2="ka",
        alpha_3="geo",
        bibliographic="geo",
        terminology="kat",
    )
    KAT = LanguageUnit(
        name="Georgian",
        alpha_2="ka",
        alpha_3="kat",
        bibliographic="geo",
        terminology="kat",
    )
    GEZ = LanguageUnit(
        name="Geez",
        alpha_2=None,
        alpha_3="gez",
        bibliographic=None,
        terminology="gez",
    )
    GIL = LanguageUnit(
        name="Gilbertese",
        alpha_2=None,
        alpha_3="gil",
        bibliographic=None,
        terminology="gil",
    )
    GLA = LanguageUnit(
        name="Gaelic; Scottish Gaelic",
        alpha_2="gd",
        alpha_3="gla",
        bibliographic=None,
        terminology="gla",
    )
    GLE = LanguageUnit(
        name="Irish",
        alpha_2="ga",
        alpha_3="gle",
        bibliographic=None,
        terminology="gle",
    )
    GLG = LanguageUnit(
        name="Galician",
        alpha_2="gl",
        alpha_3="glg",
        bibliographic=None,
        terminology="glg",
    )
    GLV = LanguageUnit(
        name="Manx",
        alpha_2="gv",
        alpha_3="glv",
        bibliographic=None,
        terminology="glv",
    )
    GMH = LanguageUnit(
        name="German, Middle High (ca.1050-1500)",
        alpha_2=None,
        alpha_3="gmh",
        bibliographic=None,
        terminology="gmh",
    )
    GOH = LanguageUnit(
        name="German, Old High (ca.750-1050)",
        alpha_2=None,
        alpha_3="goh",
        bibliographic=None,
        terminology="goh",
    )
    GON = LanguageUnit(
        name="Gondi",
        alpha_2=None,
        alpha_3="gon",
        bibliographic=None,
        terminology="gon",
    )
    GOR = LanguageUnit(
        name="Gorontalo",
        alpha_2=None,
        alpha_3="gor",
        bibliographic=None,
        terminology="gor",
    )
    GOT = LanguageUnit(
        name="Gothic",
        alpha_2=None,
        alpha_3="got",
        bibliographic=None,
        terminology="got",
    )
    GRB = LanguageUnit(
        name="Grebo",
        alpha_2=None,
        alpha_3="grb",
        bibliographic=None,
        terminology="grb",
    )
    GRC = LanguageUnit(
        name="Greek, Ancient (to 1453)",
        alpha_2=None,
        alpha_3="grc",
        bibliographic=None,
        terminology="grc",
    )
    GRN = LanguageUnit(
        name="Guarani",
        alpha_2="gn",
        alpha_3="grn",
        bibliographic=None,
        terminology="grn",
    )
    GSW = LanguageUnit(
        name="Swiss German; Alemannic; Alsatian",
        alpha_2=None,
        alpha_3="gsw",
        bibliographic=None,
        terminology="gsw",
    )
    GUJ = LanguageUnit(
        name="Gujarati",
        alpha_2="gu",
        alpha_3="guj",
        bibliographic=None,
        terminology="guj",
    )
    GWI = LanguageUnit(
        name="Gwich'in",
        alpha_2=None,
        alpha_3="gwi",
        bibliographic=None,
        terminology="gwi",
    )
    HAI = LanguageUnit(
        name="Haida",
        alpha_2=None,
        alpha_3="hai",
        bibliographic=None,
        terminology="hai",
    )
    HAT = LanguageUnit(
        name="Haitian; Haitian Creole",
        alpha_2="ht",
        alpha_3="hat",
        bibliographic=None,
        terminology="hat",
    )
    HAU = LanguageUnit(
        name="Hausa",
        alpha_2="ha",
        alpha_3="hau",
        bibliographic=None,
        terminology="hau",
    )
    HAW = LanguageUnit(
        name="Hawaiian",
        alpha_2=None,
        alpha_3="haw",
        bibliographic=None,
        terminology="haw",
    )
    HEB = LanguageUnit(
        name="Hebrew",
        alpha_2="he",
        alpha_3="heb",
        bibliographic=None,
        terminology="heb",
    )
    HER = LanguageUnit(
        name="Herero",
        alpha_2="hz",
        alpha_3="her",
        bibliographic=None,
        terminology="her",
    )
    HIL = LanguageUnit(
        name="Hiligaynon",
        alpha_2=None,
        alpha_3="hil",
        bibliographic=None,
        terminology="hil",
    )
    HIM = LanguageUnit(
        name="Himachali languages; Western Pahari languages",
        alpha_2=None,
        alpha_3="him",
        bibliographic=None,
        terminology="him",
    )
    HIN = LanguageUnit(
        name="Hindi",
        alpha_2="hi",
        alpha_3="hin",
        bibliographic=None,
        terminology="hin",
    )
    HIT = LanguageUnit(
        name="Hittite",
        alpha_2=None,
        alpha_3="hit",
        bibliographic=None,
        terminology="hit",
    )
    HMN = LanguageUnit(
        name="Hmong; Mong",
        alpha_2=None,
        alpha_3="hmn",
        bibliographic=None,
        terminology="hmn",
    )
    HMO = LanguageUnit(
        name="Hiri Motu",
        alpha_2="ho",
        alpha_3="hmo",
        bibliographic=None,
        terminology="hmo",
    )
    HRV = LanguageUnit(
        name="Croatian",
        alpha_2="hr",
        alpha_3="hrv",
        bibliographic=None,
        terminology="hrv",
    )
    HSB = LanguageUnit(
        name="Upper Sorbian",
        alpha_2=None,
        alpha_3="hsb",
        bibliographic=None,
        terminology="hsb",
    )
    HUN = LanguageUnit(
        name="Hungarian",
        alpha_2="hu",
        alpha_3="hun",
        bibliographic=None,
        terminology="hun",
    )
    HUP = LanguageUnit(
        name="Hupa",
        alpha_2=None,
        alpha_3="hup",
        bibliographic=None,
        terminology="hup",
    )
    IBA = LanguageUnit(
        name="Iban",
        alpha_2=None,
        alpha_3="iba",
        bibliographic=None,
        terminology="iba",
    )
    IBO = LanguageUnit(
        name="Igbo",
        alpha_2="ig",
        alpha_3="ibo",
        bibliographic=None,
        terminology="ibo",
    )
    ICE = LanguageUnit(
        name="Icelandic",
        alpha_2="is",
        alpha_3="ice",
        bibliographic="ice",
        terminology="isl",
    )
    ISL = LanguageUnit(
        name="Icelandic",
        alpha_2="is",
        alpha_3="isl",
        bibliographic="ice",
        terminology="isl",
    )
    IDO = LanguageUnit(
        name="Ido",
        alpha_2="io",
        alpha_3="ido",
        bibliographic=None,
        terminology="ido",
    )
    III = LanguageUnit(
        name="Sichuan Yi; Nuosu",
        alpha_2="ii",
        alpha_3="iii",
        bibliographic=None,
        terminology="iii",
    )
    IJO = LanguageUnit(
        name="Ijo languages",
        alpha_2=None,
        alpha_3="ijo",
        bibliographic=None,
        terminology="ijo",
    )
    IKU = LanguageUnit(
        name="Inuktitut",
        alpha_2="iu",
        alpha_3="iku",
        bibliographic=None,
        terminology="iku",
    )
    ILE = LanguageUnit(
        name="Interlingue; Occidental",
        alpha_2="ie",
        alpha_3="ile",
        bibliographic=None,
        terminology="ile",
    )
    ILO = LanguageUnit(
        name="Iloko",
        alpha_2=None,
        alpha_3="ilo",
        bibliographic=None,
        terminology="ilo",
    )
    INA = LanguageUnit(
        name="Interlingua (International Auxiliary Language Association)",
        alpha_2="ia",
        alpha_3="ina",
        bibliographic=None,
        terminology="ina",
    )
    INC = LanguageUnit(
        name="Indic languages",
        alpha_2=None,
        alpha_3="inc",
        bibliographic=None,
        terminology="inc",
    )
    IND = LanguageUnit(
        name="Indonesian",
        alpha_2="id",
        alpha_3="ind",
        bibliographic=None,
        terminology="ind",
    )
    INE = LanguageUnit(
        name="Indo-European languages",
        alpha_2=None,
        alpha_3="ine",
        bibliographic=None,
        terminology="ine",
    )
    INH = LanguageUnit(
        name="Ingush",
        alpha_2=None,
        alpha_3="inh",
        bibliographic=None,
        terminology="inh",
    )
    IPK = LanguageUnit(
        name="Inupiaq",
        alpha_2="ik",
        alpha_3="ipk",
        bibliographic=None,
        terminology="ipk",
    )
    IRA = LanguageUnit(
        name="Iranian languages",
        alpha_2=None,
        alpha_3="ira",
        bibliographic=None,
        terminology="ira",
    )
    IRO = LanguageUnit(
        name="Iroquoian languages",
        alpha_2=None,
        alpha_3="iro",
        bibliographic=None,
        terminology="iro",
    )
    ITA = LanguageUnit(
        name="Italian",
        alpha_2="it",
        alpha_3="ita",
        bibliographic=None,
        terminology="ita",
    )
    JAV = LanguageUnit(
        name="Javanese",
        alpha_2="jv",
        alpha_3="jav",
        bibliographic=None,
        terminology="jav",
    )
    JBO = LanguageUnit(
        name="Lojban",
        alpha_2=None,
        alpha_3="jbo",
        bibliographic=None,
        terminology="jbo",
    )
    JPN = LanguageUnit(
        name="Japanese",
        alpha_2="ja",
        alpha_3="jpn",
        bibliographic=None,
        terminology="jpn",
    )
    JPR = LanguageUnit(
        name="Judeo-Persian",
        alpha_2=None,
        alpha_3="jpr",
        bibliographic=None,
        terminology="jpr",
    )
    JRB = LanguageUnit(
        name="Judeo-Arabic",
        alpha_2=None,
        alpha_3="jrb",
        bibliographic=None,
        terminology="jrb",
    )
    KAA = LanguageUnit(
        name="Kara-Kalpak",
        alpha_2=None,
        alpha_3="kaa",
        bibliographic=None,
        terminology="kaa",
    )
    KAB = LanguageUnit(
        name="Kabyle",
        alpha_2=None,
        alpha_3="kab",
        bibliographic=None,
        terminology="kab",
    )
    KAC = LanguageUnit(
        name="Kachin; Jingpho",
        alpha_2=None,
        alpha_3="kac",
        bibliographic=None,
        terminology="kac",
    )
    KAL = LanguageUnit(
        name="Kalaallisut; Greenlandic",
        alpha_2="kl",
        alpha_3="kal",
        bibliographic=None,
        terminology="kal",
    )
    KAM = LanguageUnit(
        name="Kamba",
        alpha_2=None,
        alpha_3="kam",
        bibliographic=None,
        terminology="kam",
    )
    KAN = LanguageUnit(
        name="Kannada",
        alpha_2="kn",
        alpha_3="kan",
        bibliographic=None,
        terminology="kan",
    )
    KAR = LanguageUnit(
        name="Karen languages",
        alpha_2=None,
        alpha_3="kar",
        bibliographic=None,
        terminology="kar",
    )
    KAS = LanguageUnit(
        name="Kashmiri",
        alpha_2="ks",
        alpha_3="kas",
        bibliographic=None,
        terminology="kas",
    )
    KAU = LanguageUnit(
        name="Kanuri",
        alpha_2="kr",
        alpha_3="kau",
        bibliographic=None,
        terminology="kau",
    )
    KAW = LanguageUnit(
        name="Kawi",
        alpha_2=None,
        alpha_3="kaw",
        bibliographic=None,
        terminology="kaw",
    )
    KAZ = LanguageUnit(
        name="Kazakh",
        alpha_2="kk",
        alpha_3="kaz",
        bibliographic=None,
        terminology="kaz",
    )
    KBD = LanguageUnit(
        name="Kabardian",
        alpha_2=None,
        alpha_3="kbd",
        bibliographic=None,
        terminology="kbd",
    )
    KHA = LanguageUnit(
        name="Khasi",
        alpha_2=None,
        alpha_3="kha",
        bibliographic=None,
        terminology="kha",
    )
    KHI = LanguageUnit(
        name="Khoisan languages",
        alpha_2=None,
        alpha_3="khi",
        bibliographic=None,
        terminology="khi",
    )
    KHM = LanguageUnit(
        name="Central Khmer",
        alpha_2="km",
        alpha_3="khm",
        bibliographic=None,
        terminology="khm",
    )
    KHO = LanguageUnit(
        name="Khotanese; Sakan",
        alpha_2=None,
        alpha_3="kho",
        bibliographic=None,
        terminology="kho",
    )
    KIK = LanguageUnit(
        name="Kikuyu; Gikuyu",
        alpha_2="ki",
        alpha_3="kik",
        bibliographic=None,
        terminology="kik",
    )
    KIN = LanguageUnit(
        name="Kinyarwanda",
        alpha_2="rw",
        alpha_3="kin",
        bibliographic=None,
        terminology="kin",
    )
    KIR = LanguageUnit(
        name="Kirghiz; Kyrgyz",
        alpha_2="ky",
        alpha_3="kir",
        bibliographic=None,
        terminology="kir",
    )
    KMB = LanguageUnit(
        name="Kimbundu",
        alpha_2=None,
        alpha_3="kmb",
        bibliographic=None,
        terminology="kmb",
    )
    KOK = LanguageUnit(
        name="Konkani",
        alpha_2=None,
        alpha_3="kok",
        bibliographic=None,
        terminology="kok",
    )
    KOM = LanguageUnit(
        name="Komi",
        alpha_2="kv",
        alpha_3="kom",
        bibliographic=None,
        terminology="kom",
    )
    KON = LanguageUnit(
        name="Kongo",
        alpha_2="kg",
        alpha_3="kon",
        bibliographic=None,
        terminology="kon",
    )
    KOR = LanguageUnit(
        name="Korean",
        alpha_2="ko",
        alpha_3="kor",
        bibliographic=None,
        terminology="kor",
    )
    KOS = LanguageUnit(
        name="Kosraean",
        alpha_2=None,
        alpha_3="kos",
        bibliographic=None,
        terminology="kos",
    )
    KPE = LanguageUnit(
        name="Kpelle",
        alpha_2=None,
        alpha_3="kpe",
        bibliographic=None,
        terminology="kpe",
    )
    KRC = LanguageUnit(
        name="Karachay-Balkar",
        alpha_2=None,
        alpha_3="krc",
        bibliographic=None,
        terminology="krc",
    )
    KRL = LanguageUnit(
        name="Karelian",
        alpha_2=None,
        alpha_3="krl",
        bibliographic=None,
        terminology="krl",
    )
    KRO = LanguageUnit(
        name="Kru languages",
        alpha_2=None,
        alpha_3="kro",
        bibliographic=None,
        terminology="kro",
    )
    KRU = LanguageUnit(
        name="Kurukh",
        alpha_2=None,
        alpha_3="kru",
        bibliographic=None,
        terminology="kru",
    )
    KUA = LanguageUnit(
        name="Kuanyama; Kwanyama",
        alpha_2="kj",
        alpha_3="kua",
        bibliographic=None,
        terminology="kua",
    )
    KUM = LanguageUnit(
        name="Kumyk",
        alpha_2=None,
        alpha_3="kum",
        bibliographic=None,
        terminology="kum",
    )
    KUR = LanguageUnit(
        name="Kurdish",
        alpha_2="ku",
        alpha_3="kur",
        bibliographic=None,
        terminology="kur",
    )
    KUT = LanguageUnit(
        name="Kutenai",
        alpha_2=None,
        alpha_3="kut",
        bibliographic=None,
        terminology="kut",
    )
    LAD = LanguageUnit(
        name="Ladino",
        alpha_2=None,
        alpha_3="lad",
        bibliographic=None,
        terminology="lad",
    )
    LAH = LanguageUnit(
        name="Lahnda",
        alpha_2=None,
        alpha_3="lah",
        bibliographic=None,
        terminology="lah",
    )
    LAM = LanguageUnit(
        name="Lamba",
        alpha_2=None,
        alpha_3="lam",
        bibliographic=None,
        terminology="lam",
    )
    LAO = LanguageUnit(
        name="Lao",
        alpha_2="lo",
        alpha_3="lao",
        bibliographic=None,
        terminology="lao",
    )
    LAT = LanguageUnit(
        name="Latin",
        alpha_2="la",
        alpha_3="lat",
        bibliographic=None,
        terminology="lat",
    )
    LAV = LanguageUnit(
        name="Latvian",
        alpha_2="lv",
        alpha_3="lav",
        bibliographic=None,
        terminology="lav",
    )
    LEZ = LanguageUnit(
        name="Lezghian",
        alpha_2=None,
        alpha_3="lez",
        bibliographic=None,
        terminology="lez",
    )
    LIM = LanguageUnit(
        name="Limburgan; Limburger; Limburgish",
        alpha_2="li",
        alpha_3="lim",
        bibliographic=None,
        terminology="lim",
    )
    LIN = LanguageUnit(
        name="Lingala",
        alpha_2="ln",
        alpha_3="lin",
        bibliographic=None,
        terminology="lin",
    )
    LIT = LanguageUnit(
        name="Lithuanian",
        alpha_2="lt",
        alpha_3="lit",
        bibliographic=None,
        terminology="lit",
    )
    LOL = LanguageUnit(
        name="Mongo",
        alpha_2=None,
        alpha_3="lol",
        bibliographic=None,
        terminology="lol",
    )
    LOZ = LanguageUnit(
        name="Lozi",
        alpha_2=None,
        alpha_3="loz",
        bibliographic=None,
        terminology="loz",
    )
    LTZ = LanguageUnit(
        name="Luxembourgish; Letzeburgesch",
        alpha_2="lb",
        alpha_3="ltz",
        bibliographic=None,
        terminology="ltz",
    )
    LUA = LanguageUnit(
        name="Luba-Lulua",
        alpha_2=None,
        alpha_3="lua",
        bibliographic=None,
        terminology="lua",
    )
    LUB = LanguageUnit(
        name="Luba-Katanga",
        alpha_2="lu",
        alpha_3="lub",
        bibliographic=None,
        terminology="lub",
    )
    LUG = LanguageUnit(
        name="Ganda",
        alpha_2="lg",
        alpha_3="lug",
        bibliographic=None,
        terminology="lug",
    )
    LUI = LanguageUnit(
        name="Luiseno",
        alpha_2=None,
        alpha_3="lui",
        bibliographic=None,
        terminology="lui",
    )
    LUN = LanguageUnit(
        name="Lunda",
        alpha_2=None,
        alpha_3="lun",
        bibliographic=None,
        terminology="lun",
    )
    LUO = LanguageUnit(
        name="Luo (Kenya and Tanzania)",
        alpha_2=None,
        alpha_3="luo",
        bibliographic=None,
        terminology="luo",
    )
    LUS = LanguageUnit(
        name="Lushai",
        alpha_2=None,
        alpha_3="lus",
        bibliographic=None,
        terminology="lus",
    )
    MAC = LanguageUnit(
        name="Macedonian",
        alpha_2="mk",
        alpha_3="mac",
        bibliographic="mac",
        terminology="mkd",
    )
    MKD = LanguageUnit(
        name="Macedonian",
        alpha_2="mk",
        alpha_3="mkd",
        bibliographic="mac",
        terminology="mkd",
    )
    MAD = LanguageUnit(
        name="Madurese",
        alpha_2=None,
        alpha_3="mad",
        bibliographic=None,
        terminology="mad",
    )
    MAG = LanguageUnit(
        name="Magahi",
        alpha_2=None,
        alpha_3="mag",
        bibliographic=None,
        terminology="mag",
    )
    MAH = LanguageUnit(
        name="Marshallese",
        alpha_2="mh",
        alpha_3="mah",
        bibliographic=None,
        terminology="mah",
    )
    MAI = LanguageUnit(
        name="Maithili",
        alpha_2=None,
        alpha_3="mai",
        bibliographic=None,
        terminology="mai",
    )
    MAK = LanguageUnit(
        name="Makasar",
        alpha_2=None,
        alpha_3="mak",
        bibliographic=None,
        terminology="mak",
    )
    MAL = LanguageUnit(
        name="Malayalam",
        alpha_2="ml",
        alpha_3="mal",
        bibliographic=None,
        terminology="mal",
    )
    MAN = LanguageUnit(
        name="Mandingo",
        alpha_2=None,
        alpha_3="man",
        bibliographic=None,
        terminology="man",
    )
    MAO = LanguageUnit(
        name="Maori",
        alpha_2="mi",
        alpha_3="mao",
        bibliographic="mao",
        terminology="mri",
    )
    MRI = LanguageUnit(
        name="Maori",
        alpha_2="mi",
        alpha_3="mri",
        bibliographic="mao",
        terminology="mri",
    )
    MAP = LanguageUnit(
        name="Austronesian languages",
        alpha_2=None,
        alpha_3="map",
        bibliographic=None,
        terminology="map",
    )
    MAR = LanguageUnit(
        name="Marathi",
        alpha_2="mr",
        alpha_3="mar",
        bibliographic=None,
        terminology="mar",
    )
    MAS = LanguageUnit(
        name="Masai",
        alpha_2=None,
        alpha_3="mas",
        bibliographic=None,
        terminology="mas",
    )
    MAY = LanguageUnit(
        name="Malay",
        alpha_2="ms",
        alpha_3="may",
        bibliographic="may",
        terminology="msa",
    )
    MSA = LanguageUnit(
        name="Malay",
        alpha_2="ms",
        alpha_3="msa",
        bibliographic="may",
        terminology="msa",
    )
    MDF = LanguageUnit(
        name="Moksha",
        alpha_2=None,
        alpha_3="mdf",
        bibliographic=None,
        terminology="mdf",
    )
    MDR = LanguageUnit(
        name="Mandar",
        alpha_2=None,
        alpha_3="mdr",
        bibliographic=None,
        terminology="mdr",
    )
    MEN = LanguageUnit(
        name="Mende",
        alpha_2=None,
        alpha_3="men",
        bibliographic=None,
        terminology="men",
    )
    MGA = LanguageUnit(
        name="Irish, Middle (900-1200)",
        alpha_2=None,
        alpha_3="mga",
        bibliographic=None,
        terminology="mga",
    )
    MIC = LanguageUnit(
        name="Mi'kmaq; Micmac",
        alpha_2=None,
        alpha_3="mic",
        bibliographic=None,
        terminology="mic",
    )
    MIN = LanguageUnit(
        name="Minangkabau",
        alpha_2=None,
        alpha_3="min",
        bibliographic=None,
        terminology="min",
    )
    MIS = LanguageUnit(
        name="Uncoded languages",
        alpha_2=None,
        alpha_3="mis",
        bibliographic=None,
        terminology="mis",
    )
    MKH = LanguageUnit(
        name="Mon-Khmer languages",
        alpha_2=None,
        alpha_3="mkh",
        bibliographic=None,
        terminology="mkh",
    )
    MLG = LanguageUnit(
        name="Malagasy",
        alpha_2="mg",
        alpha_3="mlg",
        bibliographic=None,
        terminology="mlg",
    )
    MLT = LanguageUnit(
        name="Maltese",
        alpha_2="mt",
        alpha_3="mlt",
        bibliographic=None,
        terminology="mlt",
    )
    MNC = LanguageUnit(
        name="Manchu",
        alpha_2=None,
        alpha_3="mnc",
        bibliographic=None,
        terminology="mnc",
    )
    MNI = LanguageUnit(
        name="Manipuri",
        alpha_2=None,
        alpha_3="mni",
        bibliographic=None,
        terminology="mni",
    )
    MNO = LanguageUnit(
        name="Manobo languages",
        alpha_2=None,
        alpha_3="mno",
        bibliographic=None,
        terminology="mno",
    )
    MOH = LanguageUnit(
        name="Mohawk",
        alpha_2=None,
        alpha_3="moh",
        bibliographic=None,
        terminology="moh",
    )
    MON = LanguageUnit(
        name="Mongolian",
        alpha_2="mn",
        alpha_3="mon",
        bibliographic=None,
        terminology="mon",
    )
    MOS = LanguageUnit(
        name="Mossi",
        alpha_2=None,
        alpha_3="mos",
        bibliographic=None,
        terminology="mos",
    )
    MUL = LanguageUnit(
        name="Multiple languages",
        alpha_2=None,
        alpha_3="mul",
        bibliographic=None,
        terminology="mul",
    )
    MUN = LanguageUnit(
        name="Munda languages",
        alpha_2=None,
        alpha_3="mun",
        bibliographic=None,
        terminology="mun",
    )
    MUS = LanguageUnit(
        name="Creek",
        alpha_2=None,
        alpha_3="mus",
        bibliographic=None,
        terminology="mus",
    )
    MWL = LanguageUnit(
        name="Mirandese",
        alpha_2=None,
        alpha_3="mwl",
        bibliographic=None,
        terminology="mwl",
    )
    MWR = LanguageUnit(
        name="Marwari",
        alpha_2=None,
        alpha_3="mwr",
        bibliographic=None,
        terminology="mwr",
    )
    MYN = LanguageUnit(
        name="Mayan languages",
        alpha_2=None,
        alpha_3="myn",
        bibliographic=None,
        terminology="myn",
    )
    MYV = LanguageUnit(
        name="Erzya",
        alpha_2=None,
        alpha_3="myv",
        bibliographic=None,
        terminology="myv",
    )
    NAH = LanguageUnit(
        name="Nahuatl languages",
        alpha_2=None,
        alpha_3="nah",
        bibliographic=None,
        terminology="nah",
    )
    NAI = LanguageUnit(
        name="North American Indian languages",
        alpha_2=None,
        alpha_3="nai",
        bibliographic=None,
        terminology="nai",
    )
    NAP = LanguageUnit(
        name="Neapolitan",
        alpha_2=None,
        alpha_3="nap",
        bibliographic=None,
        terminology="nap",
    )
    NAU = LanguageUnit(
        name="Nauru",
        alpha_2="na",
        alpha_3="nau",
        bibliographic=None,
        terminology="nau",
    )
    NAV = LanguageUnit(
        name="Navajo; Navaho",
        alpha_2="nv",
        alpha_3="nav",
        bibliographic=None,
        terminology="nav",
    )
    NBL = LanguageUnit(
        name="Ndebele, South; South Ndebele",
        alpha_2="nr",
        alpha_3="nbl",
        bibliographic=None,
        terminology="nbl",
    )
    NDE = LanguageUnit(
        name="Ndebele, North; North Ndebele",
        alpha_2="nd",
        alpha_3="nde",
        bibliographic=None,
        terminology="nde",
    )
    NDO = LanguageUnit(
        name="Ndonga",
        alpha_2="ng",
        alpha_3="ndo",
        bibliographic=None,
        terminology="ndo",
    )
    NDS = LanguageUnit(
        name="Low German; Low Saxon; German, Low; Saxon, Low",
        alpha_2=None,
        alpha_3="nds",
        bibliographic=None,
        terminology="nds",
    )
    NEP = LanguageUnit(
        name="Nepali",
        alpha_2="ne",
        alpha_3="nep",
        bibliographic=None,
        terminology="nep",
    )
    NEW = LanguageUnit(
        name="Nepal Bhasa; Newari",
        alpha_2=None,
        alpha_3="new",
        bibliographic=None,
        terminology="new",
    )
    NIA = LanguageUnit(
        name="Nias",
        alpha_2=None,
        alpha_3="nia",
        bibliographic=None,
        terminology="nia",
    )
    NIC = LanguageUnit(
        name="Niger-Kordofanian languages",
        alpha_2=None,
        alpha_3="nic",
        bibliographic=None,
        terminology="nic",
    )
    NIU = LanguageUnit(
        name="Niuean",
        alpha_2=None,
        alpha_3="niu",
        bibliographic=None,
        terminology="niu",
    )
    NNO = LanguageUnit(
        name="Norwegian Nynorsk; Nynorsk, Norwegian",
        alpha_2="nn",
        alpha_3="nno",
        bibliographic=None,
        terminology="nno",
    )
    NOB = LanguageUnit(
        name="Bokmål, Norwegian; Norwegian Bokmål",
        alpha_2="nb",
        alpha_3="nob",
        bibliographic=None,
        terminology="nob",
    )
    NOG = LanguageUnit(
        name="Nogai",
        alpha_2=None,
        alpha_3="nog",
        bibliographic=None,
        terminology="nog",
    )
    NON = LanguageUnit(
        name="Norse, Old",
        alpha_2=None,
        alpha_3="non",
        bibliographic=None,
        terminology="non",
    )
    NOR = LanguageUnit(
        name="Norwegian",
        alpha_2="no",
        alpha_3="nor",
        bibliographic=None,
        terminology="nor",
    )
    NQO = LanguageUnit(
        name="N'Ko",
        alpha_2=None,
        alpha_3="nqo",
        bibliographic=None,
        terminology="nqo",
    )
    NSO = LanguageUnit(
        name="Pedi; Sepedi; Northern Sotho",
        alpha_2=None,
        alpha_3="nso",
        bibliographic=None,
        terminology="nso",
    )
    NUB = LanguageUnit(
        name="Nubian languages",
        alpha_2=None,
        alpha_3="nub",
        bibliographic=None,
        terminology="nub",
    )
    NWC = LanguageUnit(
        name="Classical Newari; Old Newari; Classical Nepal Bhasa",
        alpha_2=None,
        alpha_3="nwc",
        bibliographic=None,
        terminology="nwc",
    )
    NYA = LanguageUnit(
        name="Chichewa; Chewa; Nyanja",
        alpha_2="ny",
        alpha_3="nya",
        bibliographic=None,
        terminology="nya",
    )
    NYM = LanguageUnit(
        name="Nyamwezi",
        alpha_2=None,
        alpha_3="nym",
        bibliographic=None,
        terminology="nym",
    )
    NYN = LanguageUnit(
        name="Nyankole",
        alpha_2=None,
        alpha_3="nyn",
        bibliographic=None,
        terminology="nyn",
    )
    NYO = LanguageUnit(
        name="Nyoro",
        alpha_2=None,
        alpha_3="nyo",
        bibliographic=None,
        terminology="nyo",
    )
    NZI = LanguageUnit(
        name="Nzima",
        alpha_2=None,
        alpha_3="nzi",
        bibliographic=None,
        terminology="nzi",
    )
    OCI = LanguageUnit(
        name="Occitan (post 1500)",
        alpha_2="oc",
        alpha_3="oci",
        bibliographic=None,
        terminology="oci",
    )
    OJI = LanguageUnit(
        name="Ojibwa",
        alpha_2="oj",
        alpha_3="oji",
        bibliographic=None,
        terminology="oji",
    )
    ORI = LanguageUnit(
        name="Oriya",
        alpha_2="or",
        alpha_3="ori",
        bibliographic=None,
        terminology="ori",
    )
    ORM = LanguageUnit(
        name="Oromo",
        alpha_2="om",
        alpha_3="orm",
        bibliographic=None,
        terminology="orm",
    )
    OSA = LanguageUnit(
        name="Osage",
        alpha_2=None,
        alpha_3="osa",
        bibliographic=None,
        terminology="osa",
    )
    OSS = LanguageUnit(
        name="Ossetian; Ossetic",
        alpha_2="os",
        alpha_3="oss",
        bibliographic=None,
        terminology="oss",
    )
    OTA = LanguageUnit(
        name="Turkish, Ottoman (1500-1928)",
        alpha_2=None,
        alpha_3="ota",
        bibliographic=None,
        terminology="ota",
    )
    OTO = LanguageUnit(
        name="Otomian languages",
        alpha_2=None,
        alpha_3="oto",
        bibliographic=None,
        terminology="oto",
    )
    PAA = LanguageUnit(
        name="Papuan languages",
        alpha_2=None,
        alpha_3="paa",
        bibliographic=None,
        terminology="paa",
    )
    PAG = LanguageUnit(
        name="Pangasinan",
        alpha_2=None,
        alpha_3="pag",
        bibliographic=None,
        terminology="pag",
    )
    PAL = LanguageUnit(
        name="Pahlavi",
        alpha_2=None,
        alpha_3="pal",
        bibliographic=None,
        terminology="pal",
    )
    PAM = LanguageUnit(
        name="Pampanga; Kapampangan",
        alpha_2=None,
        alpha_3="pam",
        bibliographic=None,
        terminology="pam",
    )
    PAN = LanguageUnit(
        name="Panjabi; Punjabi",
        alpha_2="pa",
        alpha_3="pan",
        bibliographic=None,
        terminology="pan",
    )
    PAP = LanguageUnit(
        name="Papiamento",
        alpha_2=None,
        alpha_3="pap",
        bibliographic=None,
        terminology="pap",
    )
    PAU = LanguageUnit(
        name="Palauan",
        alpha_2=None,
        alpha_3="pau",
        bibliographic=None,
        terminology="pau",
    )
    PEO = LanguageUnit(
        name="Persian, Old (ca.600-400 B.C.)",
        alpha_2=None,
        alpha_3="peo",
        bibliographic=None,
        terminology="peo",
    )
    PHI = LanguageUnit(
        name="Philippine languages",
        alpha_2=None,
        alpha_3="phi",
        bibliographic=None,
        terminology="phi",
    )
    PHN = LanguageUnit(
        name="Phoenician",
        alpha_2=None,
        alpha_3="phn",
        bibliographic=None,
        terminology="phn",
    )
    PLI = LanguageUnit(
        name="Pali",
        alpha_2="pi",
        alpha_3="pli",
        bibliographic=None,
        terminology="pli",
    )
    POL = LanguageUnit(
        name="Polish",
        alpha_2="pl",
        alpha_3="pol",
        bibliographic=None,
        terminology="pol",
    )
    PON = LanguageUnit(
        name="Pohnpeian",
        alpha_2=None,
        alpha_3="pon",
        bibliographic=None,
        terminology="pon",
    )
    POR = LanguageUnit(
        name="Portuguese",
        alpha_2="pt",
        alpha_3="por",
        bibliographic=None,
        terminology="por",
    )
    PRA = LanguageUnit(
        name="Prakrit languages",
        alpha_2=None,
        alpha_3="pra",
        bibliographic=None,
        terminology="pra",
    )
    PRO = LanguageUnit(
        name="Provençal, Old (to 1500);Occitan, Old (to 1500)",
        alpha_2=None,
        alpha_3="pro",
        bibliographic=None,
        terminology="pro",
    )
    PUS = LanguageUnit(
        name="Pushto; Pashto",
        alpha_2="ps",
        alpha_3="pus",
        bibliographic=None,
        terminology="pus",
    )
    # QAA_QTZ = LanguageUnit(
    #     name="Reserved for local use",
    #     alpha_2=None,
    #     alpha_3="qaa-qtz",
    #     bibliographic=None,
    #     terminology="qaa-qtz",
    # )
    QUE = LanguageUnit(
        name="Quechua",
        alpha_2="qu",
        alpha_3="que",
        bibliographic=None,
        terminology="que",
    )
    RAJ = LanguageUnit(
        name="Rajasthani",
        alpha_2=None,
        alpha_3="raj",
        bibliographic=None,
        terminology="raj",
    )
    RAP = LanguageUnit(
        name="Rapanui",
        alpha_2=None,
        alpha_3="rap",
        bibliographic=None,
        terminology="rap",
    )
    RAR = LanguageUnit(
        name="Rarotongan; Cook Islands Maori",
        alpha_2=None,
        alpha_3="rar",
        bibliographic=None,
        terminology="rar",
    )
    ROA = LanguageUnit(
        name="Romance languages",
        alpha_2=None,
        alpha_3="roa",
        bibliographic=None,
        terminology="roa",
    )
    ROH = LanguageUnit(
        name="Romansh",
        alpha_2="rm",
        alpha_3="roh",
        bibliographic=None,
        terminology="roh",
    )
    ROM = LanguageUnit(
        name="Romany",
        alpha_2=None,
        alpha_3="rom",
        bibliographic=None,
        terminology="rom",
    )
    RUM = LanguageUnit(
        name="Romanian; Moldavian; Moldovan",
        alpha_2="ro",
        alpha_3="rum",
        bibliographic="rum",
        terminology="ron",
    )
    RON = LanguageUnit(
        name="Romanian; Moldavian; Moldovan",
        alpha_2="ro",
        alpha_3="ron",
        bibliographic="rum",
        terminology="ron",
    )
    RUN = LanguageUnit(
        name="Rundi",
        alpha_2="rn",
        alpha_3="run",
        bibliographic=None,
        terminology="run",
    )
    RUP = LanguageUnit(
        name="Aromanian; Arumanian; Macedo-Romanian",
        alpha_2=None,
        alpha_3="rup",
        bibliographic=None,
        terminology="rup",
    )
    RUS = LanguageUnit(
        name="Russian",
        alpha_2="ru",
        alpha_3="rus",
        bibliographic=None,
        terminology="rus",
    )
    SAD = LanguageUnit(
        name="Sandawe",
        alpha_2=None,
        alpha_3="sad",
        bibliographic=None,
        terminology="sad",
    )
    SAG = LanguageUnit(
        name="Sango",
        alpha_2="sg",
        alpha_3="sag",
        bibliographic=None,
        terminology="sag",
    )
    SAH = LanguageUnit(
        name="Yakut",
        alpha_2=None,
        alpha_3="sah",
        bibliographic=None,
        terminology="sah",
    )
    SAI = LanguageUnit(
        name="South American Indian languages",
        alpha_2=None,
        alpha_3="sai",
        bibliographic=None,
        terminology="sai",
    )
    SAL = LanguageUnit(
        name="Salishan languages",
        alpha_2=None,
        alpha_3="sal",
        bibliographic=None,
        terminology="sal",
    )
    SAM = LanguageUnit(
        name="Samaritan Aramaic",
        alpha_2=None,
        alpha_3="sam",
        bibliographic=None,
        terminology="sam",
    )
    SAN = LanguageUnit(
        name="Sanskrit",
        alpha_2="sa",
        alpha_3="san",
        bibliographic=None,
        terminology="san",
    )
    SAS = LanguageUnit(
        name="Sasak",
        alpha_2=None,
        alpha_3="sas",
        bibliographic=None,
        terminology="sas",
    )
    SAT = LanguageUnit(
        name="Santali",
        alpha_2=None,
        alpha_3="sat",
        bibliographic=None,
        terminology="sat",
    )
    SCN = LanguageUnit(
        name="Sicilian",
        alpha_2=None,
        alpha_3="scn",
        bibliographic=None,
        terminology="scn",
    )
    SCO = LanguageUnit(
        name="Scots",
        alpha_2=None,
        alpha_3="sco",
        bibliographic=None,
        terminology="sco",
    )
    SEL = LanguageUnit(
        name="Selkup",
        alpha_2=None,
        alpha_3="sel",
        bibliographic=None,
        terminology="sel",
    )
    SEM = LanguageUnit(
        name="Semitic languages",
        alpha_2=None,
        alpha_3="sem",
        bibliographic=None,
        terminology="sem",
    )
    SGA = LanguageUnit(
        name="Irish, Old (to 900)",
        alpha_2=None,
        alpha_3="sga",
        bibliographic=None,
        terminology="sga",
    )
    SGN = LanguageUnit(
        name="Sign Languages",
        alpha_2=None,
        alpha_3="sgn",
        bibliographic=None,
        terminology="sgn",
    )
    SHN = LanguageUnit(
        name="Shan",
        alpha_2=None,
        alpha_3="shn",
        bibliographic=None,
        terminology="shn",
    )
    SID = LanguageUnit(
        name="Sidamo",
        alpha_2=None,
        alpha_3="sid",
        bibliographic=None,
        terminology="sid",
    )
    SIN = LanguageUnit(
        name="Sinhala; Sinhalese",
        alpha_2="si",
        alpha_3="sin",
        bibliographic=None,
        terminology="sin",
    )
    SIO = LanguageUnit(
        name="Siouan languages",
        alpha_2=None,
        alpha_3="sio",
        bibliographic=None,
        terminology="sio",
    )
    SIT = LanguageUnit(
        name="Sino-Tibetan languages",
        alpha_2=None,
        alpha_3="sit",
        bibliographic=None,
        terminology="sit",
    )
    SLA = LanguageUnit(
        name="Slavic languages",
        alpha_2=None,
        alpha_3="sla",
        bibliographic=None,
        terminology="sla",
    )
    SLO = LanguageUnit(
        name="Slovak",
        alpha_2="sk",
        alpha_3="slo",
        bibliographic="slo",
        terminology="slk",
    )
    SLK = LanguageUnit(
        name="Slovak",
        alpha_2="sk",
        alpha_3="slk",
        bibliographic="slo",
        terminology="slk",
    )
    SLV = LanguageUnit(
        name="Slovenian",
        alpha_2="sl",
        alpha_3="slv",
        bibliographic=None,
        terminology="slv",
    )
    SMA = LanguageUnit(
        name="Southern Sami",
        alpha_2=None,
        alpha_3="sma",
        bibliographic=None,
        terminology="sma",
    )
    SME = LanguageUnit(
        name="Northern Sami",
        alpha_2="se",
        alpha_3="sme",
        bibliographic=None,
        terminology="sme",
    )
    SMI = LanguageUnit(
        name="Sami languages",
        alpha_2=None,
        alpha_3="smi",
        bibliographic=None,
        terminology="smi",
    )
    SMJ = LanguageUnit(
        name="Lule Sami",
        alpha_2=None,
        alpha_3="smj",
        bibliographic=None,
        terminology="smj",
    )
    SMN = LanguageUnit(
        name="Inari Sami",
        alpha_2=None,
        alpha_3="smn",
        bibliographic=None,
        terminology="smn",
    )
    SMO = LanguageUnit(
        name="Samoan",
        alpha_2="sm",
        alpha_3="smo",
        bibliographic=None,
        terminology="smo",
    )
    SMS = LanguageUnit(
        name="Skolt Sami",
        alpha_2=None,
        alpha_3="sms",
        bibliographic=None,
        terminology="sms",
    )
    SNA = LanguageUnit(
        name="Shona",
        alpha_2="sn",
        alpha_3="sna",
        bibliographic=None,
        terminology="sna",
    )
    SND = LanguageUnit(
        name="Sindhi",
        alpha_2="sd",
        alpha_3="snd",
        bibliographic=None,
        terminology="snd",
    )
    SNK = LanguageUnit(
        name="Soninke",
        alpha_2=None,
        alpha_3="snk",
        bibliographic=None,
        terminology="snk",
    )
    SOG = LanguageUnit(
        name="Sogdian",
        alpha_2=None,
        alpha_3="sog",
        bibliographic=None,
        terminology="sog",
    )
    SOM = LanguageUnit(
        name="Somali",
        alpha_2="so",
        alpha_3="som",
        bibliographic=None,
        terminology="som",
    )
    SON = LanguageUnit(
        name="Songhai languages",
        alpha_2=None,
        alpha_3="son",
        bibliographic=None,
        terminology="son",
    )
    SOT = LanguageUnit(
        name="Sotho, Southern",
        alpha_2="st",
        alpha_3="sot",
        bibliographic=None,
        terminology="sot",
    )
    SPA = LanguageUnit(
        name="Spanish; Castilian",
        alpha_2="es",
        alpha_3="spa",
        bibliographic=None,
        terminology="spa",
    )
    SRD = LanguageUnit(
        name="Sardinian",
        alpha_2="sc",
        alpha_3="srd",
        bibliographic=None,
        terminology="srd",
    )
    SRN = LanguageUnit(
        name="Sranan Tongo",
        alpha_2=None,
        alpha_3="srn",
        bibliographic=None,
        terminology="srn",
    )
    SRP = LanguageUnit(
        name="Serbian",
        alpha_2="sr",
        alpha_3="srp",
        bibliographic=None,
        terminology="srp",
    )
    SRR = LanguageUnit(
        name="Serer",
        alpha_2=None,
        alpha_3="srr",
        bibliographic=None,
        terminology="srr",
    )
    SSA = LanguageUnit(
        name="Nilo-Saharan languages",
        alpha_2=None,
        alpha_3="ssa",
        bibliographic=None,
        terminology="ssa",
    )
    SSW = LanguageUnit(
        name="Swati",
        alpha_2="ss",
        alpha_3="ssw",
        bibliographic=None,
        terminology="ssw",
    )
    SUK = LanguageUnit(
        name="Sukuma",
        alpha_2=None,
        alpha_3="suk",
        bibliographic=None,
        terminology="suk",
    )
    SUN = LanguageUnit(
        name="Sundanese",
        alpha_2="su",
        alpha_3="sun",
        bibliographic=None,
        terminology="sun",
    )
    SUS = LanguageUnit(
        name="Susu",
        alpha_2=None,
        alpha_3="sus",
        bibliographic=None,
        terminology="sus",
    )
    SUX = LanguageUnit(
        name="Sumerian",
        alpha_2=None,
        alpha_3="sux",
        bibliographic=None,
        terminology="sux",
    )
    SWA = LanguageUnit(
        name="Swahili",
        alpha_2="sw",
        alpha_3="swa",
        bibliographic=None,
        terminology="swa",
    )
    SWE = LanguageUnit(
        name="Swedish",
        alpha_2="sv",
        alpha_3="swe",
        bibliographic=None,
        terminology="swe",
    )
    SYC = LanguageUnit(
        name="Classical Syriac",
        alpha_2=None,
        alpha_3="syc",
        bibliographic=None,
        terminology="syc",
    )
    SYR = LanguageUnit(
        name="Syriac",
        alpha_2=None,
        alpha_3="syr",
        bibliographic=None,
        terminology="syr",
    )
    TAH = LanguageUnit(
        name="Tahitian",
        alpha_2="ty",
        alpha_3="tah",
        bibliographic=None,
        terminology="tah",
    )
    TAI = LanguageUnit(
        name="Tai languages",
        alpha_2=None,
        alpha_3="tai",
        bibliographic=None,
        terminology="tai",
    )
    TAM = LanguageUnit(
        name="Tamil",
        alpha_2="ta",
        alpha_3="tam",
        bibliographic=None,
        terminology="tam",
    )
    TAT = LanguageUnit(
        name="Tatar",
        alpha_2="tt",
        alpha_3="tat",
        bibliographic=None,
        terminology="tat",
    )
    TEL = LanguageUnit(
        name="Telugu",
        alpha_2="te",
        alpha_3="tel",
        bibliographic=None,
        terminology="tel",
    )
    TEM = LanguageUnit(
        name="Timne",
        alpha_2=None,
        alpha_3="tem",
        bibliographic=None,
        terminology="tem",
    )
    TER = LanguageUnit(
        name="Tereno",
        alpha_2=None,
        alpha_3="ter",
        bibliographic=None,
        terminology="ter",
    )
    TET = LanguageUnit(
        name="Tetum",
        alpha_2=None,
        alpha_3="tet",
        bibliographic=None,
        terminology="tet",
    )
    TGK = LanguageUnit(
        name="Tajik",
        alpha_2="tg",
        alpha_3="tgk",
        bibliographic=None,
        terminology="tgk",
    )
    TGL = LanguageUnit(
        name="Tagalog",
        alpha_2="tl",
        alpha_3="tgl",
        bibliographic=None,
        terminology="tgl",
    )
    THA = LanguageUnit(
        name="Thai",
        alpha_2="th",
        alpha_3="tha",
        bibliographic=None,
        terminology="tha",
    )
    TIG = LanguageUnit(
        name="Tigre",
        alpha_2=None,
        alpha_3="tig",
        bibliographic=None,
        terminology="tig",
    )
    TIR = LanguageUnit(
        name="Tigrinya",
        alpha_2="ti",
        alpha_3="tir",
        bibliographic=None,
        terminology="tir",
    )
    TIV = LanguageUnit(
        name="Tiv",
        alpha_2=None,
        alpha_3="tiv",
        bibliographic=None,
        terminology="tiv",
    )
    TKL = LanguageUnit(
        name="Tokelau",
        alpha_2=None,
        alpha_3="tkl",
        bibliographic=None,
        terminology="tkl",
    )
    TLH = LanguageUnit(
        name="Klingon; tlhIngan-Hol",
        alpha_2=None,
        alpha_3="tlh",
        bibliographic=None,
        terminology="tlh",
    )
    TLI = LanguageUnit(
        name="Tlingit",
        alpha_2=None,
        alpha_3="tli",
        bibliographic=None,
        terminology="tli",
    )
    TMH = LanguageUnit(
        name="Tamashek",
        alpha_2=None,
        alpha_3="tmh",
        bibliographic=None,
        terminology="tmh",
    )
    TOG = LanguageUnit(
        name="Tonga (Nyasa)",
        alpha_2=None,
        alpha_3="tog",
        bibliographic=None,
        terminology="tog",
    )
    TON = LanguageUnit(
        name="Tonga (Tonga Islands)",
        alpha_2="to",
        alpha_3="ton",
        bibliographic=None,
        terminology="ton",
    )
    TPI = LanguageUnit(
        name="Tok Pisin",
        alpha_2=None,
        alpha_3="tpi",
        bibliographic=None,
        terminology="tpi",
    )
    TSI = LanguageUnit(
        name="Tsimshian",
        alpha_2=None,
        alpha_3="tsi",
        bibliographic=None,
        terminology="tsi",
    )
    TSN = LanguageUnit(
        name="Tswana",
        alpha_2="tn",
        alpha_3="tsn",
        bibliographic=None,
        terminology="tsn",
    )
    TSO = LanguageUnit(
        name="Tsonga",
        alpha_2="ts",
        alpha_3="tso",
        bibliographic=None,
        terminology="tso",
    )
    TUK = LanguageUnit(
        name="Turkmen",
        alpha_2="tk",
        alpha_3="tuk",
        bibliographic=None,
        terminology="tuk",
    )
    TUM = LanguageUnit(
        name="Tumbuka",
        alpha_2=None,
        alpha_3="tum",
        bibliographic=None,
        terminology="tum",
    )
    TUP = LanguageUnit(
        name="Tupi languages",
        alpha_2=None,
        alpha_3="tup",
        bibliographic=None,
        terminology="tup",
    )
    TUR = LanguageUnit(
        name="Turkish",
        alpha_2="tr",
        alpha_3="tur",
        bibliographic=None,
        terminology="tur",
    )
    TUT = LanguageUnit(
        name="Altaic languages",
        alpha_2=None,
        alpha_3="tut",
        bibliographic=None,
        terminology="tut",
    )
    TVL = LanguageUnit(
        name="Tuvalu",
        alpha_2=None,
        alpha_3="tvl",
        bibliographic=None,
        terminology="tvl",
    )
    TWI = LanguageUnit(
        name="Twi",
        alpha_2="tw",
        alpha_3="twi",
        bibliographic=None,
        terminology="twi",
    )
    TYV = LanguageUnit(
        name="Tuvinian",
        alpha_2=None,
        alpha_3="tyv",
        bibliographic=None,
        terminology="tyv",
    )
    UDM = LanguageUnit(
        name="Udmurt",
        alpha_2=None,
        alpha_3="udm",
        bibliographic=None,
        terminology="udm",
    )
    UGA = LanguageUnit(
        name="Ugaritic",
        alpha_2=None,
        alpha_3="uga",
        bibliographic=None,
        terminology="uga",
    )
    UIG = LanguageUnit(
        name="Uighur; Uyghur",
        alpha_2="ug",
        alpha_3="uig",
        bibliographic=None,
        terminology="uig",
    )
    UKR = LanguageUnit(
        name="Ukrainian",
        alpha_2="uk",
        alpha_3="ukr",
        bibliographic=None,
        terminology="ukr",
    )
    UMB = LanguageUnit(
        name="Umbundu",
        alpha_2=None,
        alpha_3="umb",
        bibliographic=None,
        terminology="umb",
    )
    UND = LanguageUnit(
        name="Undetermined",
        alpha_2=None,
        alpha_3="und",
        bibliographic=None,
        terminology="und",
    )
    URD = LanguageUnit(
        name="Urdu",
        alpha_2="ur",
        alpha_3="urd",
        bibliographic=None,
        terminology="urd",
    )
    UZB = LanguageUnit(
        name="Uzbek",
        alpha_2="uz",
        alpha_3="uzb",
        bibliographic=None,
        terminology="uzb",
    )
    VAI = LanguageUnit(
        name="Vai",
        alpha_2=None,
        alpha_3="vai",
        bibliographic=None,
        terminology="vai",
    )
    VEN = LanguageUnit(
        name="Venda",
        alpha_2="ve",
        alpha_3="ven",
        bibliographic=None,
        terminology="ven",
    )
    VIE = LanguageUnit(
        name="Vietnamese",
        alpha_2="vi",
        alpha_3="vie",
        bibliographic=None,
        terminology="vie",
    )
    VOL = LanguageUnit(
        name="Volapük",
        alpha_2="vo",
        alpha_3="vol",
        bibliographic=None,
        terminology="vol",
    )
    VOT = LanguageUnit(
        name="Votic",
        alpha_2=None,
        alpha_3="vot",
        bibliographic=None,
        terminology="vot",
    )
    WAK = LanguageUnit(
        name="Wakashan languages",
        alpha_2=None,
        alpha_3="wak",
        bibliographic=None,
        terminology="wak",
    )
    WAL = LanguageUnit(
        name="Wolaitta; Wolaytta",
        alpha_2=None,
        alpha_3="wal",
        bibliographic=None,
        terminology="wal",
    )
    WAR = LanguageUnit(
        name="Waray",
        alpha_2=None,
        alpha_3="war",
        bibliographic=None,
        terminology="war",
    )
    WAS = LanguageUnit(
        name="Washo",
        alpha_2=None,
        alpha_3="was",
        bibliographic=None,
        terminology="was",
    )
    WEN = LanguageUnit(
        name="Sorbian languages",
        alpha_2=None,
        alpha_3="wen",
        bibliographic=None,
        terminology="wen",
    )
    WLN = LanguageUnit(
        name="Walloon",
        alpha_2="wa",
        alpha_3="wln",
        bibliographic=None,
        terminology="wln",
    )
    WOL = LanguageUnit(
        name="Wolof",
        alpha_2="wo",
        alpha_3="wol",
        bibliographic=None,
        terminology="wol",
    )
    XAL = LanguageUnit(
        name="Kalmyk; Oirat",
        alpha_2=None,
        alpha_3="xal",
        bibliographic=None,
        terminology="xal",
    )
    XHO = LanguageUnit(
        name="Xhosa",
        alpha_2="xh",
        alpha_3="xho",
        bibliographic=None,
        terminology="xho",
    )
    YAO = LanguageUnit(
        name="Yao",
        alpha_2=None,
        alpha_3="yao",
        bibliographic=None,
        terminology="yao",
    )
    YAP = LanguageUnit(
        name="Yapese",
        alpha_2=None,
        alpha_3="yap",
        bibliographic=None,
        terminology="yap",
    )
    YID = LanguageUnit(
        name="Yiddish",
        alpha_2="yi",
        alpha_3="yid",
        bibliographic=None,
        terminology="yid",
    )
    YOR = LanguageUnit(
        name="Yoruba",
        alpha_2="yo",
        alpha_3="yor",
        bibliographic=None,
        terminology="yor",
    )
    YPK = LanguageUnit(
        name="Yupik languages",
        alpha_2=None,
        alpha_3="ypk",
        bibliographic=None,
        terminology="ypk",
    )
    ZAP = LanguageUnit(
        name="Zapotec",
        alpha_2=None,
        alpha_3="zap",
        bibliographic=None,
        terminology="zap",
    )
    ZBL = LanguageUnit(
        name="Blissymbols; Blissymbolics; Bliss",
        alpha_2=None,
        alpha_3="zbl",
        bibliographic=None,
        terminology="zbl",
    )
    ZEN = LanguageUnit(
        name="Zenaga",
        alpha_2=None,
        alpha_3="zen",
        bibliographic=None,
        terminology="zen",
    )
    ZGH = LanguageUnit(
        name="Standard Moroccan Tamazight",
        alpha_2=None,
        alpha_3="zgh",
        bibliographic=None,
        terminology="zgh",
    )
    ZHA = LanguageUnit(
        name="Zhuang; Chuang",
        alpha_2="za",
        alpha_3="zha",
        bibliographic=None,
        terminology="zha",
    )
    ZND = LanguageUnit(
        name="Zande languages",
        alpha_2=None,
        alpha_3="znd",
        bibliographic=None,
        terminology="znd",
    )
    ZUL = LanguageUnit(
        name="Zulu",
        alpha_2="zu",
        alpha_3="zul",
        bibliographic=None,
        terminology="zul",
    )
    ZUN = LanguageUnit(
        name="Zuni",
        alpha_2=None,
        alpha_3="zun",
        bibliographic=None,
        terminology="zun",
    )
    ZXX = LanguageUnit(
        name="No linguistic content; Not applicable",
        alpha_2=None,
        alpha_3="zxx",
        bibliographic=None,
        terminology="zxx",
    )
    ZZA = LanguageUnit(
        name="Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki",
        alpha_2=None,
        alpha_3="zza",
        bibliographic=None,
        terminology="zza",
    )

    @property
    def unit(self) -> LanguageUnit:
        """
        Returns:
            ``pycountries.languages.LanguageUnit``.
        """
        return self._value_

    @property
    def alpha_2(self) -> str | None:
        """
        Returns:
            ISO 639-1 Alpha 2 code. Can be ``None``.
        """
        return self.unit.alpha_2

    @property
    def alpha_3(self) -> str:
        """
        Returns:
            ISO 639-2 Alpha 3 code.
        """
        return self.unit.alpha_3

    @property
    def value(self) -> str:
        """
        Returns:
            ISO 639-2 Alpha 3 code.
        """
        return self.unit.alpha_3

    @property
    def bibliographic(self) -> str | None:
        """
        Returns:
            ISO 639-2 Alpha 3 bibliographic code.
        """
        return self.unit.bibliographic

    @property
    def terminology(self) -> str:
        """
        Returns:
            ISO 639-2 Alpha 3 terminology code.
        """
        return self.unit.terminology

    def __str__(self) -> str:
        return self.value
