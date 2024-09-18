from __future__ import annotations

import sys
from enum import Enum
from functools import singledispatchmethod
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from pycountries._base import EnumTypeBase
from pycountries.countries import Country

if TYPE_CHECKING:
    from types import MappingProxyType


class PhoneUnitBase(BaseModel):
    country: Country
    calling_code: int = Field(
        description="International calling code",
    )
    # prefixes: list[int]  # Abstract property

    def is_prefix_supported(self, prefix: int, /) -> bool:
        if not self.prefixes or prefix is None:
            return True
        return prefix in self.prefixes


if sys.version_info >= (3, 10):  # noqa: UP036

    class PhoneUnit(PhoneUnitBase):
        prefixes: list[int]
else:
    from typing import List  # noqa: UP035

    class PhoneUnit(PhoneUnitBase):
        prefixes: List[int]  # noqa: UP006


class _PhoneUnitNotFoundError(Exception):
    """Phone Unit Not Found Error"""


class _PhoneEnumType(EnumTypeBase):
    @singledispatchmethod
    def _normalize_value(cls, value: str | int, /) -> int:  # noqa: N805
        raise ValueError(f'"{value}" has wrong type. Should be str or int') from None

    @_normalize_value.register
    def _(cls, value: str, /) -> int:  # noqa: N805
        if value.startswith("+"):
            value = value.split("+")[1]
        try:
            return int(value)
        except (TypeError, ValueError):
            raise ValueError(f'"{value}" has unsupported type. Supported examples: "+1", "1"') from None

    @_normalize_value.register
    def _(cls, value: int, /) -> int:  # noqa: N805
        return value

    @classmethod
    def get_phone(
        cls,
        value: int,
        members: MappingProxyType[str, Phone],
        /,
        *,
        prefix: int | None,
    ) -> Phone:
        candidates: list[Phone] = []
        phone: Phone
        for _, phone in members.items():
            if value == phone.calling_code:
                if phone.prefixes and phone.is_prefix_supported(prefix):
                    return phone
                if not phone.prefixes:
                    candidates.append(phone)

        try:
            # Return first available candidate
            # TODO: Maybe return phone with maximum prefixes?
            return candidates[0]
        except IndexError:
            raise _PhoneUnitNotFoundError() from None

    def __call__(cls, value: str | int, prefix: int | None = None, *args, **kw):  # type: ignore[override] # noqa: N805
        members: MappingProxyType[str, Phone] = cls.__members__.values().mapping  # type: ignore[attr-defined]
        normalized_value: int = cls._normalize_value(value)
        try:
            return cls.get_phone(normalized_value, members, prefix=prefix)
        except _PhoneUnitNotFoundError:
            raise ValueError(f'"{value}" is not a valid {cls.__qualname__}') from None


class Phone(Enum, metaclass=_PhoneEnumType):
    BD = PhoneUnit(
        country=Country.BD.value,
        calling_code=880,
        prefixes=[],
    )
    BE = PhoneUnit(
        country=Country.BE.value,
        calling_code=32,
        prefixes=[],
    )
    BF = PhoneUnit(
        country=Country.BF.value,
        calling_code=226,
        prefixes=[],
    )
    BG = PhoneUnit(
        country=Country.BG.value,
        calling_code=359,
        prefixes=[],
    )
    BA = PhoneUnit(
        country=Country.BA.value,
        calling_code=387,
        prefixes=[],
    )
    BB = PhoneUnit(
        country=Country.BB.value,
        calling_code=1,
        prefixes=[
            246,
        ],
    )
    WF = PhoneUnit(
        country=Country.WF.value,
        calling_code=681,
        prefixes=[],
    )
    BL = PhoneUnit(
        country=Country.BL.value,
        calling_code=590,
        prefixes=[],
    )
    BM = PhoneUnit(
        country=Country.BM.value,
        calling_code=1,
        prefixes=[
            441,
        ],
    )
    BN = PhoneUnit(
        country=Country.BN.value,
        calling_code=673,
        prefixes=[],
    )
    BO = PhoneUnit(
        country=Country.BO.value,
        calling_code=591,
        prefixes=[],
    )
    BH = PhoneUnit(
        country=Country.BH.value,
        calling_code=973,
        prefixes=[],
    )
    BI = PhoneUnit(
        country=Country.BI.value,
        calling_code=257,
        prefixes=[],
    )
    BJ = PhoneUnit(
        country=Country.BJ.value,
        calling_code=229,
        prefixes=[],
    )
    BT = PhoneUnit(
        country=Country.BT.value,
        calling_code=975,
        prefixes=[],
    )
    JM = PhoneUnit(
        country=Country.JM.value,
        calling_code=1,
        prefixes=[
            876,
        ],
    )
    # BV = PhoneUnit(
    #     country=Country.BV.value,
    #     calling_code=None,
    #     prefixes=[],
    # )
    BW = PhoneUnit(
        country=Country.BW.value,
        calling_code=267,
        prefixes=[],
    )
    WS = PhoneUnit(
        country=Country.WS.value,
        calling_code=685,
        prefixes=[],
    )
    BQ = PhoneUnit(
        country=Country.BQ.value,
        calling_code=599,
        prefixes=[],
    )
    BR = PhoneUnit(
        country=Country.BR.value,
        calling_code=55,
        prefixes=[],
    )
    BS = PhoneUnit(
        country=Country.BS.value,
        calling_code=1,
        prefixes=[
            242,
        ],
    )
    JE = PhoneUnit(
        country=Country.JE.value,
        calling_code=44,
        prefixes=[
            1534,
        ],
    )
    BY = PhoneUnit(
        country=Country.BY.value,
        calling_code=375,
        prefixes=[],
    )
    BZ = PhoneUnit(
        country=Country.BZ.value,
        calling_code=501,
        prefixes=[],
    )
    RU = PhoneUnit(
        country=Country.RU.value,
        calling_code=7,
        prefixes=[],
    )
    RW = PhoneUnit(
        country=Country.RW.value,
        calling_code=250,
        prefixes=[],
    )
    RS = PhoneUnit(
        country=Country.RS.value,
        calling_code=381,
        prefixes=[],
    )
    TL = PhoneUnit(
        country=Country.TL.value,
        calling_code=670,
        prefixes=[],
    )
    RE = PhoneUnit(
        country=Country.RE.value,
        calling_code=262,
        prefixes=[],
    )
    TM = PhoneUnit(
        country=Country.TM.value,
        calling_code=993,
        prefixes=[],
    )
    TJ = PhoneUnit(
        country=Country.TJ.value,
        calling_code=992,
        prefixes=[],
    )
    RO = PhoneUnit(
        country=Country.RO.value,
        calling_code=40,
        prefixes=[],
    )
    TK = PhoneUnit(
        country=Country.TK.value,
        calling_code=690,
        prefixes=[],
    )
    GW = PhoneUnit(
        country=Country.GW.value,
        calling_code=245,
        prefixes=[],
    )
    GU = PhoneUnit(
        country=Country.GU.value,
        calling_code=1,
        prefixes=[
            671,
        ],
    )
    GT = PhoneUnit(
        country=Country.GT.value,
        calling_code=502,
        prefixes=[],
    )
    # GS = PhoneUnit(
    #     country=Country.GS.value,
    #     calling_code=None,
    #     prefixes=[],
    # )
    GR = PhoneUnit(
        country=Country.GR.value,
        calling_code=30,
        prefixes=[],
    )
    GQ = PhoneUnit(
        country=Country.GQ.value,
        calling_code=240,
        prefixes=[],
    )
    GP = PhoneUnit(
        country=Country.GP.value,
        calling_code=590,
        prefixes=[],
    )
    JP = PhoneUnit(
        country=Country.JP.value,
        calling_code=81,
        prefixes=[],
    )
    GY = PhoneUnit(
        country=Country.GY.value,
        calling_code=592,
        prefixes=[],
    )
    GG = PhoneUnit(
        country=Country.GG.value,
        calling_code=44,
        prefixes=[
            1481,
        ],
    )
    GF = PhoneUnit(
        country=Country.GF.value,
        calling_code=594,
        prefixes=[],
    )
    GE = PhoneUnit(
        country=Country.GE.value,
        calling_code=995,
        prefixes=[],
    )
    GD = PhoneUnit(
        country=Country.GD.value,
        calling_code=1,
        prefixes=[
            473,
        ],
    )
    GB = PhoneUnit(
        country=Country.GB.value,
        calling_code=44,
        prefixes=[
            1224,
            1235,
            1339,
            1252,
            1507,
            1259,
            1420,
            1269,
            1264,
            1461,
            1241,
            1294,
            1301,
            1276,
            1335,
            1364,
            1233,
            1297,
            1296,
            1292,
            1295,
            1330,
            1261,
            1248,
            1341,
            1226,
            1271,
            1229,
            1446,
            1246,
            1225,
            1506,
            1234,
            1434,
            1289,
            1299,
            1237,
            121,
            1388,
            1279,
            1254,
            1253,
            1250,
            1258,
            1208,
            1204,
            1423,
            1205,
            1202,
            1451,
            1344,
            1274,
            1376,
            1356,
            1277,
            1278,
            1262,
            1308,
            1273,
            117,
            1275,
            1471,
            1508,
            1280,
            1288,
            1395,
            1425,
            1282,
            1543,
            1283,
            1284,
            1298,
            1286,
            1223,
            1227,
            29,
            1239,
            1228,
            1267,
            1556,
            1300,
            1460,
            1245,
            1242,
            1244,
            1246,
            1243,
            1249,
            1285,
            1255,
            1200,
            1437,
            1530,
            1236,
            1206,
            1492,
            1260,
            1477,
            1207,
            1257,
            1490,
            24,
            1340,
            1363,
            1270,
            1263,
            1290,
            1325,
            1332,
            1362,
            1380,
            1349,
            1379,
            1485,
            1354,
            1302,
            1305,
            1304,
            1366,
            1377,
            1398,
            1389,
            1387,
            1368,
            1382,
            1383,
            1350,
            1369,
            1361,
            191,
            1453,
            1347,
            1342,
            1355,
            1357,
            1323,
            1470,
            131,
            1343,
            1358,
            1353,
            1372,
            1392,
            1328,
            1324,
            1326,
            1329,
            1489,
            1367,
            1348,
            1303,
            1561,
            1307,
            1309,
            1320,
            1397,
            1381,
            1346,
            1373,
            1427,
            1445,
            1465,
            141,
            1458,
            1456,
            1457,
            1452,
            1408,
            1405,
            1476,
            1479,
            1474,
            1371,
            1488,
            1493,
            1475,
            1472,
            1483,
            1287,
            1422,
            1501,
            1429,
            1428,
            1424,
            1433,
            1440,
            1450,
            1497,
            1444,
            1435,
            1436,
            1431,
            1439,
            1432,
            1494,
            1455,
            1462,
            1406,
            1409,
            1407,
            1400,
            1404,
            1403,
            1484,
            1482,
            1480,
            1466,
            1464,
            1499,
            1463,
            1467,
            1473,
            1505,
            1535,
            1542,
            1573,
            1539,
            1536,
            1538,
            1360,
            1567,
            1469,
            1563,
            1553,
            1548,
            1544,
            1540,
            1577,
            1557,
            1575,
            1438,
            1547,
            1565,
            1337,
            1528,
            1549,
            1570,
            1555,
            1524,
            1564,
            1578,
            1566,
            113,
            116,
            1525,
            1568,
            1522,
            151,
            1545,
            1558,
            1550,
            1559,
            1554,
            1520,
            1546,
            1571,
            1576,
            20,
            1503,
            1509,
            1502,
            161,
            1430,
            1442,
            1526,
            1352,
            1560,
            1491,
            1293,
            1306,
            28,
            115,
            1572,
            1359,
            1333,
            1334,
            1495,
            1443,
            1496,
            1478,
            23,
            1454,
            118,
            1527,
            1209,
            114,
            1291,
            1394,
            1529,
            1268,
            1375,
            1569,
            1384,
            1386,
            1562,
            1449,
            1322,
            1487,
            1327,
        ],
    )
    GA = PhoneUnit(
        country=Country.GA.value,
        calling_code=241,
        prefixes=[],
    )
    SV = PhoneUnit(
        country=Country.SV.value,
        calling_code=503,
        prefixes=[],
    )
    GN = PhoneUnit(
        country=Country.GN.value,
        calling_code=224,
        prefixes=[],
    )
    GM = PhoneUnit(
        country=Country.GM.value,
        calling_code=220,
        prefixes=[],
    )
    GL = PhoneUnit(
        country=Country.GL.value,
        calling_code=299,
        prefixes=[],
    )
    GI = PhoneUnit(
        country=Country.GI.value,
        calling_code=350,
        prefixes=[],
    )
    GH = PhoneUnit(
        country=Country.GH.value,
        calling_code=233,
        prefixes=[],
    )
    OM = PhoneUnit(
        country=Country.OM.value,
        calling_code=968,
        prefixes=[],
    )
    TN = PhoneUnit(
        country=Country.TN.value,
        calling_code=216,
        prefixes=[],
    )
    JO = PhoneUnit(
        country=Country.JO.value,
        calling_code=962,
        prefixes=[],
    )
    HR = PhoneUnit(
        country=Country.HR.value,
        calling_code=385,
        prefixes=[],
    )
    HT = PhoneUnit(
        country=Country.HT.value,
        calling_code=509,
        prefixes=[],
    )
    HU = PhoneUnit(
        country=Country.HU.value,
        calling_code=36,
        prefixes=[],
    )
    HK = PhoneUnit(
        country=Country.HK.value,
        calling_code=852,
        prefixes=[],
    )
    HN = PhoneUnit(
        country=Country.HN.value,
        calling_code=504,
        prefixes=[],
    )
    # HM = PhoneUnit(
    #     country=Country.HM.value,
    #     calling_code=None,
    #     prefixes=[],
    # )
    VE = PhoneUnit(
        country=Country.VE.value,
        calling_code=58,
        prefixes=[],
    )
    PR = PhoneUnit(
        country=Country.PR.value,
        calling_code=1,
        prefixes=[
            787,
            939,
        ],
    )
    PS = PhoneUnit(
        country=Country.PS.value,
        calling_code=970,
        prefixes=[],
    )
    PW = PhoneUnit(
        country=Country.PW.value,
        calling_code=680,
        prefixes=[],
    )
    PT = PhoneUnit(
        country=Country.PT.value,
        calling_code=351,
        prefixes=[],
    )
    SJ = PhoneUnit(
        country=Country.SJ.value,
        calling_code=47,
        prefixes=[],
    )
    PY = PhoneUnit(
        country=Country.PY.value,
        calling_code=595,
        prefixes=[],
    )
    IQ = PhoneUnit(
        country=Country.IQ.value,
        calling_code=964,
        prefixes=[],
    )
    PA = PhoneUnit(
        country=Country.PA.value,
        calling_code=507,
        prefixes=[],
    )
    PF = PhoneUnit(
        country=Country.PF.value,
        calling_code=689,
        prefixes=[],
    )
    PG = PhoneUnit(
        country=Country.PG.value,
        calling_code=675,
        prefixes=[],
    )
    PE = PhoneUnit(
        country=Country.PE.value,
        calling_code=51,
        prefixes=[],
    )
    PK = PhoneUnit(
        country=Country.PK.value,
        calling_code=92,
        prefixes=[],
    )
    PH = PhoneUnit(
        country=Country.PH.value,
        calling_code=63,
        prefixes=[],
    )
    PN = PhoneUnit(
        country=Country.PN.value,
        calling_code=870,
        prefixes=[],
    )
    PL = PhoneUnit(
        country=Country.PL.value,
        calling_code=48,
        prefixes=[],
    )
    PM = PhoneUnit(
        country=Country.PM.value,
        calling_code=508,
        prefixes=[],
    )
    ZM = PhoneUnit(
        country=Country.ZM.value,
        calling_code=260,
        prefixes=[],
    )
    EH = PhoneUnit(
        country=Country.EH.value,
        calling_code=212,
        prefixes=[],
    )
    EE = PhoneUnit(
        country=Country.EE.value,
        calling_code=372,
        prefixes=[],
    )
    EG = PhoneUnit(
        country=Country.EG.value,
        calling_code=20,
        prefixes=[],
    )
    ZA = PhoneUnit(
        country=Country.ZA.value,
        calling_code=27,
        prefixes=[],
    )
    EC = PhoneUnit(
        country=Country.EC.value,
        calling_code=593,
        prefixes=[],
    )
    IT = PhoneUnit(
        country=Country.IT.value,
        calling_code=39,
        prefixes=[],
    )
    VN = PhoneUnit(
        country=Country.VN.value,
        calling_code=84,
        prefixes=[],
    )
    SB = PhoneUnit(
        country=Country.SB.value,
        calling_code=677,
        prefixes=[],
    )
    ET = PhoneUnit(
        country=Country.ET.value,
        calling_code=251,
        prefixes=[],
    )
    SO = PhoneUnit(
        country=Country.SO.value,
        calling_code=252,
        prefixes=[],
    )
    ZW = PhoneUnit(
        country=Country.ZW.value,
        calling_code=263,
        prefixes=[],
    )
    SA = PhoneUnit(
        country=Country.SA.value,
        calling_code=966,
        prefixes=[],
    )
    ES = PhoneUnit(
        country=Country.ES.value,
        calling_code=34,
        prefixes=[],
    )
    ER = PhoneUnit(
        country=Country.ER.value,
        calling_code=291,
        prefixes=[],
    )
    ME = PhoneUnit(
        country=Country.ME.value,
        calling_code=382,
        prefixes=[],
    )
    MD = PhoneUnit(
        country=Country.MD.value,
        calling_code=373,
        prefixes=[],
    )
    MG = PhoneUnit(
        country=Country.MG.value,
        calling_code=261,
        prefixes=[],
    )
    MF = PhoneUnit(
        country=Country.MF.value,
        calling_code=590,
        prefixes=[],
    )
    MA = PhoneUnit(
        country=Country.MA.value,
        calling_code=212,
        prefixes=[],
    )
    MC = PhoneUnit(
        country=Country.MC.value,
        calling_code=377,
        prefixes=[],
    )
    UZ = PhoneUnit(
        country=Country.UZ.value,
        calling_code=998,
        prefixes=[],
    )
    MM = PhoneUnit(
        country=Country.MM.value,
        calling_code=95,
        prefixes=[],
    )
    ML = PhoneUnit(
        country=Country.ML.value,
        calling_code=223,
        prefixes=[],
    )
    MO = PhoneUnit(
        country=Country.MO.value,
        calling_code=853,
        prefixes=[],
    )
    MN = PhoneUnit(
        country=Country.MN.value,
        calling_code=976,
        prefixes=[],
    )
    MH = PhoneUnit(
        country=Country.MH.value,
        calling_code=692,
        prefixes=[],
    )
    MK = PhoneUnit(
        country=Country.MK.value,
        calling_code=389,
        prefixes=[],
    )
    MU = PhoneUnit(
        country=Country.MU.value,
        calling_code=230,
        prefixes=[],
    )
    MT = PhoneUnit(
        country=Country.MT.value,
        calling_code=356,
        prefixes=[],
    )
    MW = PhoneUnit(
        country=Country.MW.value,
        calling_code=265,
        prefixes=[],
    )
    MV = PhoneUnit(
        country=Country.MV.value,
        calling_code=960,
        prefixes=[],
    )
    MQ = PhoneUnit(
        country=Country.MQ.value,
        calling_code=596,
        prefixes=[],
    )
    MP = PhoneUnit(
        country=Country.MP.value,
        calling_code=1,
        prefixes=[
            670,
        ],
    )
    MS = PhoneUnit(
        country=Country.MS.value,
        calling_code=1,
        prefixes=[
            664,
        ],
    )
    MR = PhoneUnit(
        country=Country.MR.value,
        calling_code=222,
        prefixes=[],
    )
    IM = PhoneUnit(
        country=Country.IM.value,
        calling_code=44,
        prefixes=[
            1624,
        ],
    )
    UG = PhoneUnit(
        country=Country.UG.value,
        calling_code=256,
        prefixes=[],
    )
    TZ = PhoneUnit(
        country=Country.TZ.value,
        calling_code=255,
        prefixes=[],
    )
    MY = PhoneUnit(
        country=Country.MY.value,
        calling_code=60,
        prefixes=[],
    )
    MX = PhoneUnit(
        country=Country.MX.value,
        calling_code=52,
        prefixes=[],
    )
    IL = PhoneUnit(
        country=Country.IL.value,
        calling_code=972,
        prefixes=[],
    )
    FR = PhoneUnit(
        country=Country.FR.value,
        calling_code=33,
        prefixes=[],
    )
    IO = PhoneUnit(
        country=Country.IO.value,
        calling_code=246,
        prefixes=[],
    )
    SH = PhoneUnit(
        country=Country.SH.value,
        calling_code=290,
        prefixes=[],
    )
    FI = PhoneUnit(
        country=Country.FI.value,
        calling_code=358,
        prefixes=[],
    )
    FJ = PhoneUnit(
        country=Country.FJ.value,
        calling_code=679,
        prefixes=[],
    )
    FK = PhoneUnit(
        country=Country.FK.value,
        calling_code=500,
        prefixes=[],
    )
    FM = PhoneUnit(
        country=Country.FM.value,
        calling_code=691,
        prefixes=[],
    )
    FO = PhoneUnit(
        country=Country.FO.value,
        calling_code=298,
        prefixes=[],
    )
    NI = PhoneUnit(
        country=Country.NI.value,
        calling_code=505,
        prefixes=[],
    )
    NL = PhoneUnit(
        country=Country.NL.value,
        calling_code=31,
        prefixes=[],
    )
    NO = PhoneUnit(
        country=Country.NO.value,
        calling_code=47,
        prefixes=[],
    )
    NA = PhoneUnit(
        country=Country.NA.value,
        calling_code=264,
        prefixes=[],
    )
    VU = PhoneUnit(
        country=Country.VU.value,
        calling_code=678,
        prefixes=[],
    )
    NC = PhoneUnit(
        country=Country.NC.value,
        calling_code=687,
        prefixes=[],
    )
    NE = PhoneUnit(
        country=Country.NE.value,
        calling_code=227,
        prefixes=[],
    )
    NF = PhoneUnit(
        country=Country.NF.value,
        calling_code=672,
        prefixes=[],
    )
    NG = PhoneUnit(
        country=Country.NG.value,
        calling_code=234,
        prefixes=[],
    )
    NZ = PhoneUnit(
        country=Country.NZ.value,
        calling_code=64,
        prefixes=[],
    )
    NP = PhoneUnit(
        country=Country.NP.value,
        calling_code=977,
        prefixes=[],
    )
    NR = PhoneUnit(
        country=Country.NR.value,
        calling_code=674,
        prefixes=[],
    )
    NU = PhoneUnit(
        country=Country.NU.value,
        calling_code=683,
        prefixes=[],
    )
    CK = PhoneUnit(
        country=Country.CK.value,
        calling_code=682,
        prefixes=[],
    )
    # XK = PhoneUnit(
    #     country=Country.XK.value,
    #     calling_code=None,
    #     prefixes=[],
    # )
    CI = PhoneUnit(
        country=Country.CI.value,
        calling_code=225,
        prefixes=[],
    )
    CH = PhoneUnit(
        country=Country.CH.value,
        calling_code=41,
        prefixes=[],
    )
    CO = PhoneUnit(
        country=Country.CO.value,
        calling_code=57,
        prefixes=[],
    )
    CN = PhoneUnit(
        country=Country.CN.value,
        calling_code=86,
        prefixes=[],
    )
    CM = PhoneUnit(
        country=Country.CM.value,
        calling_code=237,
        prefixes=[],
    )
    CL = PhoneUnit(
        country=Country.CL.value,
        calling_code=56,
        prefixes=[],
    )
    CC = PhoneUnit(
        country=Country.CC.value,
        calling_code=61,
        prefixes=[],
    )
    CA = PhoneUnit(
        country=Country.CA.value,
        calling_code=1,
        prefixes=[
            587,
            403,
            780,
            819,
            902,
            226,
            519,
            289,
            905,
            438,
            514,
            343,
            613,
            418,
            581,
            306,
            705,
            249,
            600,
            506,
            709,
            450,
            579,
            807,
            647,
            416,
            236,
            778,
            604,
            250,
            204,
            867,
        ],
    )
    CG = PhoneUnit(
        country=Country.CG.value,
        calling_code=242,
        prefixes=[],
    )
    CF = PhoneUnit(
        country=Country.CF.value,
        calling_code=236,
        prefixes=[],
    )
    CD = PhoneUnit(
        country=Country.CD.value,
        calling_code=243,
        prefixes=[],
    )
    CZ = PhoneUnit(
        country=Country.CZ.value,
        calling_code=420,
        prefixes=[],
    )
    CY = PhoneUnit(
        country=Country.CY.value,
        calling_code=357,
        prefixes=[],
    )
    CX = PhoneUnit(
        country=Country.CX.value,
        calling_code=61,
        prefixes=[],
    )
    CR = PhoneUnit(
        country=Country.CR.value,
        calling_code=506,
        prefixes=[],
    )
    CW = PhoneUnit(
        country=Country.CW.value,
        calling_code=599,
        prefixes=[],
    )
    CV = PhoneUnit(
        country=Country.CV.value,
        calling_code=238,
        prefixes=[],
    )
    CU = PhoneUnit(
        country=Country.CU.value,
        calling_code=53,
        prefixes=[],
    )
    SZ = PhoneUnit(
        country=Country.SZ.value,
        calling_code=268,
        prefixes=[],
    )
    SY = PhoneUnit(
        country=Country.SY.value,
        calling_code=963,
        prefixes=[],
    )
    SX = PhoneUnit(
        country=Country.SX.value,
        calling_code=599,
        prefixes=[],
    )
    KG = PhoneUnit(
        country=Country.KG.value,
        calling_code=996,
        prefixes=[],
    )
    KE = PhoneUnit(
        country=Country.KE.value,
        calling_code=254,
        prefixes=[],
    )
    SS = PhoneUnit(
        country=Country.SS.value,
        calling_code=211,
        prefixes=[],
    )
    SR = PhoneUnit(
        country=Country.SR.value,
        calling_code=597,
        prefixes=[],
    )
    KI = PhoneUnit(
        country=Country.KI.value,
        calling_code=686,
        prefixes=[],
    )
    KH = PhoneUnit(
        country=Country.KH.value,
        calling_code=855,
        prefixes=[],
    )
    KN = PhoneUnit(
        country=Country.KN.value,
        calling_code=1,
        prefixes=[
            869,
        ],
    )
    KM = PhoneUnit(
        country=Country.KM.value,
        calling_code=269,
        prefixes=[],
    )
    ST = PhoneUnit(
        country=Country.ST.value,
        calling_code=239,
        prefixes=[],
    )
    SK = PhoneUnit(
        country=Country.SK.value,
        calling_code=421,
        prefixes=[],
    )
    KR = PhoneUnit(
        country=Country.KR.value,
        calling_code=82,
        prefixes=[],
    )
    SI = PhoneUnit(
        country=Country.SI.value,
        calling_code=386,
        prefixes=[],
    )
    KP = PhoneUnit(
        country=Country.KP.value,
        calling_code=850,
        prefixes=[],
    )
    KW = PhoneUnit(
        country=Country.KW.value,
        calling_code=965,
        prefixes=[],
    )
    SN = PhoneUnit(
        country=Country.SN.value,
        calling_code=221,
        prefixes=[],
    )
    SM = PhoneUnit(
        country=Country.SM.value,
        calling_code=378,
        prefixes=[],
    )
    SL = PhoneUnit(
        country=Country.SL.value,
        calling_code=232,
        prefixes=[],
    )
    SC = PhoneUnit(
        country=Country.SC.value,
        calling_code=248,
        prefixes=[],
    )
    KZ = PhoneUnit(
        country=Country.KZ.value,
        calling_code=7,
        prefixes=[
            317,
            329,
            313,
            327,
            330,
            717,
            312,
            321,
            314,
            324,
            336,
            318,
            315,
            322,
            325,
            328,
            311,
            323,
            326,
            310,
        ],
    )
    KY = PhoneUnit(
        country=Country.KY.value,
        calling_code=1,
        prefixes=[
            345,
        ],
    )
    SG = PhoneUnit(
        country=Country.SG.value,
        calling_code=65,
        prefixes=[],
    )
    SE = PhoneUnit(
        country=Country.SE.value,
        calling_code=46,
        prefixes=[],
    )
    SD = PhoneUnit(
        country=Country.SD.value,
        calling_code=249,
        prefixes=[],
    )
    DO = PhoneUnit(
        country=Country.DO.value,
        calling_code=1,
        prefixes=[
            809,
            829,
        ],
    )
    DM = PhoneUnit(
        country=Country.DM.value,
        calling_code=1,
        prefixes=[
            767,
        ],
    )
    DJ = PhoneUnit(
        country=Country.DJ.value,
        calling_code=253,
        prefixes=[],
    )
    DK = PhoneUnit(
        country=Country.DK.value,
        calling_code=45,
        prefixes=[],
    )
    VG = PhoneUnit(
        country=Country.VG.value,
        calling_code=1,
        prefixes=[
            284,
        ],
    )
    DE = PhoneUnit(
        country=Country.DE.value,
        calling_code=49,
        prefixes=[],
    )
    YE = PhoneUnit(
        country=Country.YE.value,
        calling_code=967,
        prefixes=[],
    )
    DZ = PhoneUnit(
        country=Country.DZ.value,
        calling_code=213,
        prefixes=[],
    )
    US = PhoneUnit(
        country=Country.US.value,
        calling_code=1,
        prefixes=[
            325,
            330,
            234,
            518,
            229,
            957,
            505,
            320,
            730,
            618,
            657,
            909,
            752,
            714,
            907,
            734,
            278,
            703,
            571,
            828,
            606,
            404,
            770,
            678,
            470,
            609,
            762,
            706,
            331,
            737,
            512,
            667,
            443,
            410,
            225,
            425,
            360,
            240,
            610,
            484,
            835,
            406,
            228,
            659,
            205,
            952,
            208,
            857,
            617,
            802,
            631,
            203,
            475,
            718,
            347,
            979,
            818,
            747,
            856,
            239,
            319,
            447,
            217,
            843,
            681,
            304,
            980,
            704,
            423,
            872,
            773,
            312,
            413,
            708,
            464,
            283,
            513,
            931,
            440,
            216,
            573,
            803,
            614,
            380,
            925,
            361,
            214,
            972,
            469,
            764,
            650,
            276,
            563,
            937,
            386,
            940,
            720,
            303,
            313,
            679,
            620,
            218,
            715,
            534,
            848,
            732,
            915,
            908,
            607,
            814,
            760,
            442,
            541,
            458,
            812,
            701,
            910,
            810,
            954,
            754,
            479,
            260,
            682,
            817,
            559,
            352,
            409,
            219,
            970,
            616,
            231,
            920,
            274,
            336,
            864,
            254,
            985,
            959,
            860,
            516,
            808,
            832,
            713,
            281,
            938,
            256,
            936,
            317,
            515,
            949,
            769,
            601,
            731,
            904,
            551,
            201,
            870,
            913,
            975,
            816,
            308,
            262,
            845,
            865,
            337,
            765,
            863,
            717,
            740,
            517,
            307,
            956,
            575,
            702,
            580,
            859,
            501,
            562,
            323,
            310,
            213,
            502,
            978,
            351,
            806,
            434,
            339,
            781,
            478,
            608,
            603,
            507,
            660,
            641,
            830,
            901,
            786,
            305,
            414,
            612,
            251,
            334,
            630,
            615,
            724,
            504,
            917,
            646,
            212,
            973,
            862,
            716,
            510,
            341,
            432,
            405,
            531,
            402,
            927,
            689,
            407,
            321,
            269,
            364,
            270,
            445,
            267,
            215,
            623,
            602,
            480,
            878,
            412,
            763,
            626,
            248,
            772,
            971,
            503,
            207,
            401,
            719,
            919,
            984,
            530,
            775,
            804,
            951,
            540,
            585,
            309,
            815,
            779,
            252,
            916,
            989,
            831,
            801,
            385,
            210,
            935,
            858,
            619,
            628,
            415,
            408,
            669,
            805,
            661,
            424,
            627,
            369,
            707,
            941,
            906,
            912,
            570,
            206,
            564,
            318,
            301,
            227,
            712,
            605,
            574,
            509,
            417,
            636,
            435,
            314,
            557,
            651,
            727,
            662,
            209,
            209,
            315,
            253,
            850,
            813,
            419,
            567,
            785,
            947,
            520,
            918,
            430,
            903,
            757,
            586,
            202,
            847,
            224,
            561,
            316,
            302,
            774,
            508,
            914,
            928,
        ],
    )
    UY = PhoneUnit(
        country=Country.UY.value,
        calling_code=598,
        prefixes=[],
    )
    YT = PhoneUnit(
        country=Country.YT.value,
        calling_code=262,
        prefixes=[],
    )
    UM = PhoneUnit(
        country=Country.UM.value,
        calling_code=1,
        prefixes=[],
    )
    LB = PhoneUnit(
        country=Country.LB.value,
        calling_code=961,
        prefixes=[],
    )
    LC = PhoneUnit(
        country=Country.LC.value,
        calling_code=1,
        prefixes=[
            758,
        ],
    )
    LA = PhoneUnit(
        country=Country.LA.value,
        calling_code=856,
        prefixes=[],
    )
    TV = PhoneUnit(
        country=Country.TV.value,
        calling_code=688,
        prefixes=[],
    )
    TW = PhoneUnit(
        country=Country.TW.value,
        calling_code=886,
        prefixes=[],
    )
    TT = PhoneUnit(
        country=Country.TT.value,
        calling_code=1,
        prefixes=[
            868,
        ],
    )
    TR = PhoneUnit(
        country=Country.TR.value,
        calling_code=90,
        prefixes=[],
    )
    LK = PhoneUnit(
        country=Country.LK.value,
        calling_code=94,
        prefixes=[],
    )
    LI = PhoneUnit(
        country=Country.LI.value,
        calling_code=423,
        prefixes=[],
    )
    LV = PhoneUnit(
        country=Country.LV.value,
        calling_code=371,
        prefixes=[],
    )
    TO = PhoneUnit(
        country=Country.TO.value,
        calling_code=676,
        prefixes=[],
    )
    LT = PhoneUnit(
        country=Country.LT.value,
        calling_code=370,
        prefixes=[],
    )
    LU = PhoneUnit(
        country=Country.LU.value,
        calling_code=352,
        prefixes=[],
    )
    LR = PhoneUnit(
        country=Country.LR.value,
        calling_code=231,
        prefixes=[],
    )
    LS = PhoneUnit(
        country=Country.LS.value,
        calling_code=266,
        prefixes=[],
    )
    TH = PhoneUnit(
        country=Country.TH.value,
        calling_code=66,
        prefixes=[],
    )
    # TF = PhoneUnit(
    #     country=Country.TF.value,
    #     calling_code=None,
    #     prefixes=[],
    # )
    TG = PhoneUnit(
        country=Country.TG.value,
        calling_code=228,
        prefixes=[],
    )
    TD = PhoneUnit(
        country=Country.TD.value,
        calling_code=235,
        prefixes=[],
    )
    TC = PhoneUnit(
        country=Country.TC.value,
        calling_code=1,
        prefixes=[
            649,
        ],
    )
    LY = PhoneUnit(
        country=Country.LY.value,
        calling_code=218,
        prefixes=[],
    )
    VA = PhoneUnit(
        country=Country.VA.value,
        calling_code=379,
        prefixes=[],
    )
    VC = PhoneUnit(
        country=Country.VC.value,
        calling_code=1,
        prefixes=[
            784,
        ],
    )
    AE = PhoneUnit(
        country=Country.AE.value,
        calling_code=971,
        prefixes=[],
    )
    AD = PhoneUnit(
        country=Country.AD.value,
        calling_code=376,
        prefixes=[],
    )
    AG = PhoneUnit(
        country=Country.AG.value,
        calling_code=1,
        prefixes=[
            268,
        ],
    )
    AF = PhoneUnit(
        country=Country.AF.value,
        calling_code=93,
        prefixes=[],
    )
    AI = PhoneUnit(
        country=Country.AI.value,
        calling_code=1,
        prefixes=[
            264,
        ],
    )
    VI = PhoneUnit(
        country=Country.VI.value,
        calling_code=1,
        prefixes=[
            340,
        ],
    )
    IS = PhoneUnit(
        country=Country.IS.value,
        calling_code=354,
        prefixes=[],
    )
    IR = PhoneUnit(
        country=Country.IR.value,
        calling_code=98,
        prefixes=[],
    )
    AM = PhoneUnit(
        country=Country.AM.value,
        calling_code=374,
        prefixes=[],
    )
    AL = PhoneUnit(
        country=Country.AL.value,
        calling_code=355,
        prefixes=[],
    )
    AO = PhoneUnit(
        country=Country.AO.value,
        calling_code=244,
        prefixes=[],
    )
    # AQ = PhoneUnit(
    #     country=Country.AQ.value,
    #     calling_code=None,
    #     prefixes=[],
    # )
    AS = PhoneUnit(
        country=Country.AS.value,
        calling_code=1,
        prefixes=[
            684,
        ],
    )
    AR = PhoneUnit(
        country=Country.AR.value,
        calling_code=54,
        prefixes=[],
    )
    AU = PhoneUnit(
        country=Country.AU.value,
        calling_code=61,
        prefixes=[],
    )
    AT = PhoneUnit(
        country=Country.AT.value,
        calling_code=43,
        prefixes=[],
    )
    AW = PhoneUnit(
        country=Country.AW.value,
        calling_code=297,
        prefixes=[],
    )
    IN = PhoneUnit(
        country=Country.IN.value,
        calling_code=91,
        prefixes=[],
    )
    AX = PhoneUnit(
        country=Country.AX.value,
        calling_code=358,
        prefixes=[
            18,
        ],
    )
    AZ = PhoneUnit(
        country=Country.AZ.value,
        calling_code=994,
        prefixes=[],
    )
    IE = PhoneUnit(
        country=Country.IE.value,
        calling_code=353,
        prefixes=[],
    )
    ID = PhoneUnit(
        country=Country.ID.value,
        calling_code=62,
        prefixes=[],
    )
    UA = PhoneUnit(
        country=Country.UA.value,
        calling_code=380,
        prefixes=[],
    )
    QA = PhoneUnit(
        country=Country.QA.value,
        calling_code=974,
        prefixes=[],
    )
    MZ = PhoneUnit(
        country=Country.MZ.value,
        calling_code=258,
        prefixes=[],
    )

    @property
    def unit(self) -> PhoneUnit:
        """
        Returns:
            ``pycountries.phones.PhoneUnit``.
        """
        return self._value_

    @property
    def country(self) -> Country:
        """
        Returns:
            ``pycountries.countries.CountryUnit``.
        """
        return self.unit.country

    @property
    def calling_code(self) -> int:
        """
        Returns:
            int: International calling code.
        """
        return self.unit.calling_code

    @property
    def value(self) -> int:
        """
        Returns:
            ISO 3166-1 Alpha 2 code.
        """
        return self.unit.calling_code

    @property
    def prefixes(self) -> list[int]:
        return self.unit.prefixes

    def is_prefix_supported(self, prefix: int | None, /) -> bool:
        if prefix is None:
            return True
        return self.unit.is_prefix_supported(prefix)

    def __str__(self) -> str:
        return str(self.value)
