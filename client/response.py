from dataclasses import dataclass, fields, field
from typing import TypeVar, Generic, List, get_args

T = TypeVar('T')


@dataclass
class Response(Generic[T]):
    code: int
    payload: List[T]
    msg: str

    def is_success(self) -> bool:
        return self.code == 0


@dataclass
class Detail:
    availBal: str
    availEq: str
    borrowFroz: str
    cashBal: str
    ccy: str
    crossLiab: str
    disEq: str
    eq: str
    eqUsd: str
    fixedBal: str
    frozenBal: str


@dataclass
class AccountData:
    adjEq: str
    borrowFroz: str
    details: List[Detail]
    imr: str
    isoEq: str
    mgnRatio: str
    mmr: str
    notionalUsd: str
    ordFroz: str
    totalEq: str
    uTime: str
    upl: str


@dataclass
class Balance:
    availBal: str
    bal: str
    ccy: str
    frozenBal: str


@dataclass
class SubAccountData:
    canTransOut: bool
    enable: bool
    frozenFunc: List[str]
    gAuth: bool
    label: str
    mobile: str
    subAcct: str
    ts: str
    type: str
    uid: str


@dataclass
class Transfer:
    transId: str
    ccy: str
    clientId: str
    amt: str


@dataclass
class OrderStatus:
    clOrdId: str
    ordId: str
    ts: str
    sCode: str
    tag: str = ""
    sMsg: str = ""


def map_response_to_data(response: dict, data_class: Generic[T]) -> Response[T]:
    def filter_keys(item: dict, data_class_arg: Generic[T]) -> dict:
        field_names = {data_field.name for data_field in fields(data_class_arg)}
        filtered_item = {k: v for k, v in item.items() if k in field_names}

        for field_name, field_type in data_class_arg.__annotations__.items():
            if hasattr(field_type, '__origin__') and field_type.__origin__ == list:
                item_class = get_args(field_type)[0]
                filtered_item[field_name] = [item_class(**filter_keys(sub_item, item_class)) for sub_item in
                                             item.get(field_name, [])]

        return filtered_item

    data_list = [data_class(**filter_keys(item, data_class)) for item in response.get('data', [])]
    return Response(code=int(response['code']), payload=data_list, msg=response['msg'])
