from __future__ import annotations

from enum import Enum
from typing import ClassVar, Literal

from pydantic import BaseModel, Field

from pycountries._base import EnumTypeBase


class MacroLanguageUnit(BaseModel):
    m_id: str = Field(
        description="The identifier for a macrolanguage.",
        min_length=3,
        max_length=3,
    )
    i_status: Literal["A", "R"] = Field(
        description="A(active) or R(retired) indicating the status of the individual code element.",
    )


def _is_macro_language_valid(
    val: str,
    language: MacroLanguage,
    i_status: Literal["A", "R"] | None,
) -> bool:
    """
    Args:
        val: ``m_id`` to check.
        language: ``pycountries.macro_languages.MacroLanguage``.
        i_status: A(active), R(retired) or None.

    Returns:
        True if val (m_id) is appropriate and False otherwise.
    """
    if language.m_id != val:
        return False

    if i_status is None or language.i_status == i_status:
        return True

    return False


class _MacroLanguageUnitEnumType(EnumTypeBase):
    allowed_i_statuses: ClassVar[tuple[str, ...]] = (
        "A",
        "R",
    )

    def _validate_i_status(cls, i_status: str | None) -> None:  # noqa: N805
        """
        Sanity check on i_status.
        The only allowed values are A(active) and R(retired).
        """
        if i_status is not None and i_status not in cls.allowed_i_statuses:
            raise ValueError(
                f'"{i_status}" is not a valid i_status for {cls.__qualname__}. '
                f'Allowed values are: {", ".join(cls.allowed_i_statuses)}.'
            ) from None

    def __call__(cls, value, *args, i_status: Literal["A", "R"] | None = None, **kw):  # noqa: N805
        """
        Find Macro Languages by ``m_id``. Also, you can specify i_status. For example,
        if you want to retrieve retired ARA languages, you can use the next code:
        ``MacroLanguage("ara", i_status="R")``.

        Args:
            value: m_id, Case insensitive.
            *args: Other data.
            i_status (=None): A(active) and R(retired). Other values are prohibited.
            **kw: Other data.

        Returns:
            The list of ``pycountries.macro_languages.MacroLanguage``.
            If languages not found ValueError will be raised.
        """
        cls._validate_i_status(i_status)

        val: str = value.lower()
        languages: list[MacroLanguage] = []

        members = cls.__members__.values()  # type: ignore[var-annotated]
        language: MacroLanguage
        for language in members:
            if _is_macro_language_valid(val, language, i_status):
                languages.append(language)

        if languages:
            return languages

        raise ValueError(f'"{value}" is not a valid {cls.__qualname__}') from None


class MacroLanguage(Enum, metaclass=_MacroLanguageUnitEnumType):
    FAT = MacroLanguageUnit(
        m_id="aka",
        i_status="A",
    )
    TWI = MacroLanguageUnit(
        m_id="aka",
        i_status="A",
    )
    AAO = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ABH = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ABV = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ACM = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ACQ = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ACW = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ACX = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ACY = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ADF = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AEB = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AEC = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AFB = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AJP = MacroLanguageUnit(
        m_id="ara",
        i_status="R",
    )
    APC = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    APD = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ARB = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ARQ = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ARS = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ARY = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    ARZ = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AUZ = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AVL = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AYH = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AYL = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AYN = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AYP = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    BBZ = MacroLanguageUnit(
        m_id="ara",
        i_status="R",
    )
    PGA = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    SHU = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    SSH = MacroLanguageUnit(
        m_id="ara",
        i_status="A",
    )
    AYC = MacroLanguageUnit(
        m_id="aym",
        i_status="A",
    )
    AYR = MacroLanguageUnit(
        m_id="aym",
        i_status="A",
    )
    AZB = MacroLanguageUnit(
        m_id="aze",
        i_status="A",
    )
    AZJ = MacroLanguageUnit(
        m_id="aze",
        i_status="A",
    )
    BCC = MacroLanguageUnit(
        m_id="bal",
        i_status="A",
    )
    BGN = MacroLanguageUnit(
        m_id="bal",
        i_status="A",
    )
    BGP = MacroLanguageUnit(
        m_id="bal",
        i_status="A",
    )
    BCL = MacroLanguageUnit(
        m_id="bik",
        i_status="A",
    )
    BHK = MacroLanguageUnit(
        m_id="bik",
        i_status="R",
    )
    BLN = MacroLanguageUnit(
        m_id="bik",
        i_status="A",
    )
    BTO = MacroLanguageUnit(
        m_id="bik",
        i_status="A",
    )
    CTS = MacroLanguageUnit(
        m_id="bik",
        i_status="A",
    )
    FBL = MacroLanguageUnit(
        m_id="bik",
        i_status="A",
    )
    LBL = MacroLanguageUnit(
        m_id="bik",
        i_status="A",
    )
    RBL = MacroLanguageUnit(
        m_id="bik",
        i_status="A",
    )
    UBL = MacroLanguageUnit(
        m_id="bik",
        i_status="A",
    )
    EBK = MacroLanguageUnit(
        m_id="bnc",
        i_status="A",
    )
    LBK = MacroLanguageUnit(
        m_id="bnc",
        i_status="A",
    )
    OBK = MacroLanguageUnit(
        m_id="bnc",
        i_status="A",
    )
    RBK = MacroLanguageUnit(
        m_id="bnc",
        i_status="A",
    )
    VBK = MacroLanguageUnit(
        m_id="bnc",
        i_status="A",
    )
    BXM = MacroLanguageUnit(
        m_id="bua",
        i_status="A",
    )
    BXR = MacroLanguageUnit(
        m_id="bua",
        i_status="A",
    )
    BXU = MacroLanguageUnit(
        m_id="bua",
        i_status="A",
    )
    MHR = MacroLanguageUnit(
        m_id="chm",
        i_status="A",
    )
    MRJ = MacroLanguageUnit(
        m_id="chm",
        i_status="A",
    )
    CRJ = MacroLanguageUnit(
        m_id="cre",
        i_status="A",
    )
    CRK = MacroLanguageUnit(
        m_id="cre",
        i_status="A",
    )
    CRL = MacroLanguageUnit(
        m_id="cre",
        i_status="A",
    )
    CRM = MacroLanguageUnit(
        m_id="cre",
        i_status="A",
    )
    CSW = MacroLanguageUnit(
        m_id="cre",
        i_status="A",
    )
    CWD = MacroLanguageUnit(
        m_id="cre",
        i_status="A",
    )
    UMU = MacroLanguageUnit(
        m_id="del",
        i_status="A",
    )
    UNM = MacroLanguageUnit(
        m_id="del",
        i_status="A",
    )
    SCS = MacroLanguageUnit(
        m_id="den",
        i_status="A",
    )
    XSL = MacroLanguageUnit(
        m_id="den",
        i_status="A",
    )
    DIB = MacroLanguageUnit(
        m_id="din",
        i_status="A",
    )
    DIK = MacroLanguageUnit(
        m_id="din",
        i_status="A",
    )
    DIP = MacroLanguageUnit(
        m_id="din",
        i_status="A",
    )
    DIW = MacroLanguageUnit(
        m_id="din",
        i_status="A",
    )
    DKS = MacroLanguageUnit(
        m_id="din",
        i_status="A",
    )
    DGO = MacroLanguageUnit(
        m_id="doi",
        i_status="A",
    )
    XNR = MacroLanguageUnit(
        m_id="doi",
        i_status="A",
    )
    EKK = MacroLanguageUnit(
        m_id="est",
        i_status="A",
    )
    VRO = MacroLanguageUnit(
        m_id="est",
        i_status="A",
    )
    PES = MacroLanguageUnit(
        m_id="fas",
        i_status="A",
    )
    PRS = MacroLanguageUnit(
        m_id="fas",
        i_status="A",
    )
    FFM = MacroLanguageUnit(
        m_id="ful",
        i_status="A",
    )
    FUB = MacroLanguageUnit(
        m_id="ful",
        i_status="A",
    )
    FUC = MacroLanguageUnit(
        m_id="ful",
        i_status="A",
    )
    FUE = MacroLanguageUnit(
        m_id="ful",
        i_status="A",
    )
    FUF = MacroLanguageUnit(
        m_id="ful",
        i_status="A",
    )
    FUH = MacroLanguageUnit(
        m_id="ful",
        i_status="A",
    )
    FUI = MacroLanguageUnit(
        m_id="ful",
        i_status="A",
    )
    FUQ = MacroLanguageUnit(
        m_id="ful",
        i_status="A",
    )
    FUV = MacroLanguageUnit(
        m_id="ful",
        i_status="A",
    )
    BDT = MacroLanguageUnit(
        m_id="gba",
        i_status="A",
    )
    GBP = MacroLanguageUnit(
        m_id="gba",
        i_status="A",
    )
    GBQ = MacroLanguageUnit(
        m_id="gba",
        i_status="A",
    )
    GMM = MacroLanguageUnit(
        m_id="gba",
        i_status="A",
    )
    GSO = MacroLanguageUnit(
        m_id="gba",
        i_status="A",
    )
    GYA = MacroLanguageUnit(
        m_id="gba",
        i_status="A",
    )
    MDO = MacroLanguageUnit(
        m_id="gba",
        i_status="R",
    )
    ESG = MacroLanguageUnit(
        m_id="gon",
        i_status="A",
    )
    GGO = MacroLanguageUnit(
        m_id="gon",
        i_status="R",
    )
    GNO = MacroLanguageUnit(
        m_id="gon",
        i_status="A",
    )
    WSG = MacroLanguageUnit(
        m_id="gon",
        i_status="A",
    )
    GBO = MacroLanguageUnit(
        m_id="grb",
        i_status="A",
    )
    GEC = MacroLanguageUnit(
        m_id="grb",
        i_status="A",
    )
    GRJ = MacroLanguageUnit(
        m_id="grb",
        i_status="A",
    )
    GRV = MacroLanguageUnit(
        m_id="grb",
        i_status="A",
    )
    GRY = MacroLanguageUnit(
        m_id="grb",
        i_status="A",
    )
    GNW = MacroLanguageUnit(
        m_id="grn",
        i_status="A",
    )
    GUG = MacroLanguageUnit(
        m_id="grn",
        i_status="A",
    )
    GUI = MacroLanguageUnit(
        m_id="grn",
        i_status="A",
    )
    GUN = MacroLanguageUnit(
        m_id="grn",
        i_status="A",
    )
    NHD = MacroLanguageUnit(
        m_id="grn",
        i_status="A",
    )
    HAX = MacroLanguageUnit(
        m_id="hai",
        i_status="A",
    )
    HDN = MacroLanguageUnit(
        m_id="hai",
        i_status="A",
    )
    BOS = MacroLanguageUnit(
        m_id="hbs",
        i_status="A",
    )
    CNR = MacroLanguageUnit(
        m_id="hbs",
        i_status="A",
    )
    HRV = MacroLanguageUnit(
        m_id="hbs",
        i_status="A",
    )
    SRP = MacroLanguageUnit(
        m_id="hbs",
        i_status="A",
    )
    BLU = MacroLanguageUnit(
        m_id="hmn",
        i_status="R",
    )
    CQD = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HEA = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMA = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMC = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMD = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HME = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMG = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMH = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMI = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMJ = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HML = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMM = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMP = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMQ = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMS = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMW = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMY = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HMZ = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HNJ = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HRM = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    HUJ = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    MMR = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    MUQ = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    MWW = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    SFM = MacroLanguageUnit(
        m_id="hmn",
        i_status="A",
    )
    IKE = MacroLanguageUnit(
        m_id="iku",
        i_status="A",
    )
    IKT = MacroLanguageUnit(
        m_id="iku",
        i_status="A",
    )
    ESI = MacroLanguageUnit(
        m_id="ipk",
        i_status="A",
    )
    ESK = MacroLanguageUnit(
        m_id="ipk",
        i_status="A",
    )
    AJT = MacroLanguageUnit(
        m_id="jrb",
        i_status="R",
    )
    AJU = MacroLanguageUnit(
        m_id="jrb",
        i_status="A",
    )
    JYE = MacroLanguageUnit(
        m_id="jrb",
        i_status="A",
    )
    YHD = MacroLanguageUnit(
        m_id="jrb",
        i_status="A",
    )
    YUD = MacroLanguageUnit(
        m_id="jrb",
        i_status="A",
    )
    KBY = MacroLanguageUnit(
        m_id="kau",
        i_status="A",
    )
    KNC = MacroLanguageUnit(
        m_id="kau",
        i_status="A",
    )
    KRT = MacroLanguageUnit(
        m_id="kau",
        i_status="A",
    )
    ENB = MacroLanguageUnit(
        m_id="kln",
        i_status="A",
    )
    EYO = MacroLanguageUnit(
        m_id="kln",
        i_status="A",
    )
    NIQ = MacroLanguageUnit(
        m_id="kln",
        i_status="A",
    )
    OKI = MacroLanguageUnit(
        m_id="kln",
        i_status="A",
    )
    PKO = MacroLanguageUnit(
        m_id="kln",
        i_status="A",
    )
    SGC = MacroLanguageUnit(
        m_id="kln",
        i_status="A",
    )
    SPY = MacroLanguageUnit(
        m_id="kln",
        i_status="A",
    )
    TEC = MacroLanguageUnit(
        m_id="kln",
        i_status="A",
    )
    TUY = MacroLanguageUnit(
        m_id="kln",
        i_status="A",
    )
    GOM = MacroLanguageUnit(
        m_id="kok",
        i_status="A",
    )
    KNN = MacroLanguageUnit(
        m_id="kok",
        i_status="A",
    )
    KOI = MacroLanguageUnit(
        m_id="kom",
        i_status="A",
    )
    KPV = MacroLanguageUnit(
        m_id="kom",
        i_status="A",
    )
    KNG = MacroLanguageUnit(
        m_id="kon",
        i_status="A",
    )
    KWY = MacroLanguageUnit(
        m_id="kon",
        i_status="A",
    )
    LDI = MacroLanguageUnit(
        m_id="kon",
        i_status="A",
    )
    GKP = MacroLanguageUnit(
        m_id="kpe",
        i_status="A",
    )
    XPE = MacroLanguageUnit(
        m_id="kpe",
        i_status="A",
    )
    CKB = MacroLanguageUnit(
        m_id="kur",
        i_status="A",
    )
    KMR = MacroLanguageUnit(
        m_id="kur",
        i_status="A",
    )
    SDH = MacroLanguageUnit(
        m_id="kur",
        i_status="A",
    )
    HND = MacroLanguageUnit(
        m_id="lah",
        i_status="A",
    )
    HNO = MacroLanguageUnit(
        m_id="lah",
        i_status="A",
    )
    JAT = MacroLanguageUnit(
        m_id="lah",
        i_status="A",
    )
    PHR = MacroLanguageUnit(
        m_id="lah",
        i_status="A",
    )
    PMU = MacroLanguageUnit(
        m_id="lah",
        i_status="R",
    )
    PNB = MacroLanguageUnit(
        m_id="lah",
        i_status="A",
    )
    SKR = MacroLanguageUnit(
        m_id="lah",
        i_status="A",
    )
    XHE = MacroLanguageUnit(
        m_id="lah",
        i_status="A",
    )
    LTG = MacroLanguageUnit(
        m_id="lav",
        i_status="A",
    )
    LVS = MacroLanguageUnit(
        m_id="lav",
        i_status="A",
    )
    BXK = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    IDA = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    LKB = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    LKO = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    LKS = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    LRI = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    LRM = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    LSM = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    LTO = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    LTS = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    LWG = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    NLE = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    NYD = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    RAG = MacroLanguageUnit(
        m_id="luy",
        i_status="A",
    )
    EMK = MacroLanguageUnit(
        m_id="man",
        i_status="A",
    )
    MKU = MacroLanguageUnit(
        m_id="man",
        i_status="A",
    )
    MLQ = MacroLanguageUnit(
        m_id="man",
        i_status="A",
    )
    MNK = MacroLanguageUnit(
        m_id="man",
        i_status="A",
    )
    MSC = MacroLanguageUnit(
        m_id="man",
        i_status="A",
    )
    MWK = MacroLanguageUnit(
        m_id="man",
        i_status="A",
    )
    MYQ = MacroLanguageUnit(
        m_id="man",
        i_status="R",
    )
    BHR = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    BJQ = MacroLanguageUnit(
        m_id="mlg",
        i_status="R",
    )
    BMM = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    BZC = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    MSH = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    PLT = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    SKG = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    TDX = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    TKG = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    TXY = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    XMV = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    XMW = MacroLanguageUnit(
        m_id="mlg",
        i_status="A",
    )
    KHK = MacroLanguageUnit(
        m_id="mon",
        i_status="A",
    )
    MVF = MacroLanguageUnit(
        m_id="mon",
        i_status="A",
    )
    BJN = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    BTJ = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    BVE = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    BVU = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    COA = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    DUP = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    HJI = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    IND = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    JAK = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    JAX = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    KVB = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    KVR = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    KXD = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    LCE = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    LCF = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    LIW = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    MAX = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    MEO = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    MFA = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    MFB = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    MIN = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    MLY = MacroLanguageUnit(
        m_id="msa",
        i_status="R",
    )
    MQG = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    MSI = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    MUI = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    ORN = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    ORS = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    PEL = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    PSE = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    TMW = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    URK = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    VKK = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    VKT = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    XMM = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    ZLM = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    ZMI = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    ZSM = MacroLanguageUnit(
        m_id="msa",
        i_status="A",
    )
    DHD = MacroLanguageUnit(
        m_id="mwr",
        i_status="A",
    )
    MTR = MacroLanguageUnit(
        m_id="mwr",
        i_status="A",
    )
    MVE = MacroLanguageUnit(
        m_id="mwr",
        i_status="A",
    )
    RWR = MacroLanguageUnit(
        m_id="mwr",
        i_status="A",
    )
    SWV = MacroLanguageUnit(
        m_id="mwr",
        i_status="A",
    )
    WRY = MacroLanguageUnit(
        m_id="mwr",
        i_status="A",
    )
    DTY = MacroLanguageUnit(
        m_id="nep",
        i_status="A",
    )
    NPI = MacroLanguageUnit(
        m_id="nep",
        i_status="A",
    )
    NNO = MacroLanguageUnit(
        m_id="nor",
        i_status="A",
    )
    NOB = MacroLanguageUnit(
        m_id="nor",
        i_status="A",
    )
    CIW = MacroLanguageUnit(
        m_id="oji",
        i_status="A",
    )
    OJB = MacroLanguageUnit(
        m_id="oji",
        i_status="A",
    )
    OJC = MacroLanguageUnit(
        m_id="oji",
        i_status="A",
    )
    OJG = MacroLanguageUnit(
        m_id="oji",
        i_status="A",
    )
    OJS = MacroLanguageUnit(
        m_id="oji",
        i_status="A",
    )
    OJW = MacroLanguageUnit(
        m_id="oji",
        i_status="A",
    )
    OTW = MacroLanguageUnit(
        m_id="oji",
        i_status="A",
    )
    ORY = MacroLanguageUnit(
        m_id="ori",
        i_status="A",
    )
    SPV = MacroLanguageUnit(
        m_id="ori",
        i_status="A",
    )
    GAX = MacroLanguageUnit(
        m_id="orm",
        i_status="A",
    )
    GAZ = MacroLanguageUnit(
        m_id="orm",
        i_status="A",
    )
    HAE = MacroLanguageUnit(
        m_id="orm",
        i_status="A",
    )
    ORC = MacroLanguageUnit(
        m_id="orm",
        i_status="A",
    )
    PBT = MacroLanguageUnit(
        m_id="pus",
        i_status="A",
    )
    PBU = MacroLanguageUnit(
        m_id="pus",
        i_status="A",
    )
    PST = MacroLanguageUnit(
        m_id="pus",
        i_status="A",
    )
    CQU = MacroLanguageUnit(
        m_id="que",
        i_status="R",
    )
    QUB = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUD = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUF = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUG = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUH = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUK = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUL = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUP = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUR = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUS = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUW = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUX = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUY = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QUZ = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVA = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVC = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVE = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVH = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVI = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVJ = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVL = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVM = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVN = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVO = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVP = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVS = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVW = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QVZ = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QWA = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QWC = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QWH = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QWS = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXA = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXC = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXH = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXL = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXN = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXO = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXP = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXR = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXT = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXU = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    QXW = MacroLanguageUnit(
        m_id="que",
        i_status="A",
    )
    BGQ = MacroLanguageUnit(
        m_id="raj",
        i_status="A",
    )
    GDA = MacroLanguageUnit(
        m_id="raj",
        i_status="A",
    )
    GJU = MacroLanguageUnit(
        m_id="raj",
        i_status="A",
    )
    HOJ = MacroLanguageUnit(
        m_id="raj",
        i_status="A",
    )
    MUP = MacroLanguageUnit(
        m_id="raj",
        i_status="A",
    )
    WBR = MacroLanguageUnit(
        m_id="raj",
        i_status="A",
    )
    RMC = MacroLanguageUnit(
        m_id="rom",
        i_status="A",
    )
    RMF = MacroLanguageUnit(
        m_id="rom",
        i_status="A",
    )
    RML = MacroLanguageUnit(
        m_id="rom",
        i_status="A",
    )
    RMN = MacroLanguageUnit(
        m_id="rom",
        i_status="A",
    )
    RMO = MacroLanguageUnit(
        m_id="rom",
        i_status="A",
    )
    RMW = MacroLanguageUnit(
        m_id="rom",
        i_status="A",
    )
    RMY = MacroLanguageUnit(
        m_id="rom",
        i_status="A",
    )
    CLS = MacroLanguageUnit(
        m_id="san",
        i_status="A",
    )
    VSN = MacroLanguageUnit(
        m_id="san",
        i_status="A",
    )
    AAE = MacroLanguageUnit(
        m_id="sqi",
        i_status="A",
    )
    AAT = MacroLanguageUnit(
        m_id="sqi",
        i_status="A",
    )
    ALN = MacroLanguageUnit(
        m_id="sqi",
        i_status="A",
    )
    ALS = MacroLanguageUnit(
        m_id="sqi",
        i_status="A",
    )
    SDC = MacroLanguageUnit(
        m_id="srd",
        i_status="A",
    )
    SDN = MacroLanguageUnit(
        m_id="srd",
        i_status="A",
    )
    SRC = MacroLanguageUnit(
        m_id="srd",
        i_status="A",
    )
    SRO = MacroLanguageUnit(
        m_id="srd",
        i_status="A",
    )
    SWC = MacroLanguageUnit(
        m_id="swa",
        i_status="A",
    )
    SWH = MacroLanguageUnit(
        m_id="swa",
        i_status="A",
    )
    AII = MacroLanguageUnit(
        m_id="syr",
        i_status="A",
    )
    CLD = MacroLanguageUnit(
        m_id="syr",
        i_status="A",
    )
    TAQ = MacroLanguageUnit(
        m_id="tmh",
        i_status="A",
    )
    THV = MacroLanguageUnit(
        m_id="tmh",
        i_status="A",
    )
    THZ = MacroLanguageUnit(
        m_id="tmh",
        i_status="A",
    )
    TTQ = MacroLanguageUnit(
        m_id="tmh",
        i_status="A",
    )
    UZN = MacroLanguageUnit(
        m_id="uzb",
        i_status="A",
    )
    UZS = MacroLanguageUnit(
        m_id="uzb",
        i_status="A",
    )
    YDD = MacroLanguageUnit(
        m_id="yid",
        i_status="A",
    )
    YIH = MacroLanguageUnit(
        m_id="yid",
        i_status="A",
    )
    ZAA = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAB = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAC = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAD = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAE = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAF = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAI = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAM = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAO = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAQ = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAR = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAS = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAT = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAV = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAW = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZAX = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZCA = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZCD = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZOO = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPA = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPB = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPC = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPD = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPE = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPF = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPG = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPH = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPI = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPJ = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPK = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPL = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPM = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPN = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPO = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPP = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPQ = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPR = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPS = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPT = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPU = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPV = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPW = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPX = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPY = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZPZ = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZSR = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTC = MacroLanguageUnit(
        m_id="zap",
        i_status="R",
    )
    ZTE = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTG = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTL = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTM = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTN = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTP = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTQ = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTS = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTT = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTU = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTX = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    ZTY = MacroLanguageUnit(
        m_id="zap",
        i_status="A",
    )
    CCX = MacroLanguageUnit(
        m_id="zha",
        i_status="R",
    )
    CCY = MacroLanguageUnit(
        m_id="zha",
        i_status="R",
    )
    ZCH = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZEH = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZGB = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZGM = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZGN = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZHD = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZHN = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZLJ = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZLN = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZLQ = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZQE = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZYB = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZYG = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZYJ = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZYN = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    ZZJ = MacroLanguageUnit(
        m_id="zha",
        i_status="A",
    )
    CDO = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    CJY = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    CMN = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    CNP = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    CPX = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    CSP = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    CZH = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    CZO = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    GAN = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    HAK = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    HSN = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    LZH = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    MNP = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    NAN = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    WUU = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    YUE = MacroLanguageUnit(
        m_id="zho",
        i_status="A",
    )
    DIQ = MacroLanguageUnit(
        m_id="zza",
        i_status="A",
    )
    KIU = MacroLanguageUnit(
        m_id="zza",
        i_status="A",
    )

    @property
    def unit(self) -> MacroLanguageUnit:
        """
        Returns:
            ``pycountries.macro_languages.MacroLanguageUnit``.
        """
        return self._value_

    @property
    def value(self) -> str:
        """
        Returns:
            3 chars. The identifier for a macrolanguage.
        """
        return self.unit.m_id

    @property
    def m_id(self) -> str:
        """
        Returns:
            3 chars. The identifier for a macrolanguage.
        """
        return self.unit.m_id

    @property
    def i_id(self) -> str:
        """
        Returns:
            3 chars. The identifier for an individual language that is a member of the macrolanguage.
        """
        return self.name

    @property
    def i_status(self) -> Literal["A", "R"]:
        """
        Returns:
            A(active) or R(retired) indicating the status of the individual code element.
        """
        return self.unit.i_status

    def __str__(self) -> str:
        return self.value
