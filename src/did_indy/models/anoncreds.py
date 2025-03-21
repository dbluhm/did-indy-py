"""AnonCreds models."""

from typing import Any, Dict, List, Literal
from pydantic import AliasChoices, BaseModel, Field


class Schema(BaseModel):
    """Schema Model."""

    issuer_id: str = Field(
        validation_alias=AliasChoices("issuerId", "issuer_id"),
        serialization_alias="issuerId",
    )
    attr_names: List[str] = Field(
        validation_alias=AliasChoices("attrNames", "attr_names"),
        serialization_alias="attrNames",
    )
    name: str
    version: str


class CredDef(BaseModel):
    """Cred Def Model."""

    issuer_id: str = Field(
        validation_alias=AliasChoices("issuerId", "issuer_id"),
        serialization_alias="issuerId",
    )
    schema_id: str = Field(
        validation_alias=AliasChoices("schemaId", "schema_id"),
        serialization_alias="schemaId",
    )
    type: Literal["CL"]
    tag: str
    value: Dict[str, Any]


class RevRegDefValue(BaseModel):
    """Rev Reg Def Value Model."""

    max_cred_num: int = Field(
        validation_alias=AliasChoices("max_cred_num", "maxCredNum"),
        serialization_alias="maxCredNum",
    )
    public_keys: Dict[str, Any] = Field(
        validation_alias=AliasChoices("public_keys", "publicKeys"),
        serialization_alias="publicKeys",
    )
    tails_hash: str = Field(
        validation_alias=AliasChoices("tails_hash", "tailsHash"),
        serialization_alias="tailsHash",
    )
    tails_location: str = Field(
        validation_alias=AliasChoices("tails_location", "tailsLocation"),
        serialization_alias="tailsLocation",
    )


class RevRegDef(BaseModel):
    """Rev Reg Def Model."""

    issuer_id: str = Field(
        validation_alias=AliasChoices("issuerId", "issuer_id"),
        serialization_alias="issuerId",
    )
    revoc_def_type: Literal["CL_ACCUM"] = Field(
        validation_alias=AliasChoices("revoc_def_type", "revocDefType"),
        serialization_alias="revocDefType",
    )
    cred_def_id: str = Field(
        validation_alias=AliasChoices("credDefId", "cred_def_id"),
        serialization_alias="credDefId",
    )
    tag: str
    value: RevRegDefValue


class RevStatusList(BaseModel):
    """Rev List Model."""

    issuer_id: str = Field(
        validation_alias=AliasChoices("issuerId", "issuer_id"),
        serialization_alias="issuerId",
    )
    rev_reg_def_id: str = Field(
        validation_alias=AliasChoices("revRegDefId", "rev_reg_def_id"),
        serialization_alias="revRegDefId",
    )
    revocation_list: list[int] = Field(
        validation_alias=AliasChoices("revocation_list", "revocationList"),
        serialization_alias="revocationList",
    )
    current_accumulator: str = Field(
        validation_alias=AliasChoices("current_accumulator", "currentAccumulator"),
        serialization_alias="currentAccumulator",
    )
    timestamp: int | None = None
