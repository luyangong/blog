Title: fix no From Error in sqlalchemy
Date: 2024-02-21 22:56
Category: article

## 代码
```python
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


from sqlalchemy import create_engine
engine = create_engine("sqlite://", echo=False)

Base.metadata.create_all(engine)

from sqlalchemy.orm import Session

with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()

# with Session(engine) as session:
    # print(session.query(User).filter(User.name == 'sandy').all())

def raise_error():
    from sqlalchemy import exists, and_

    print(session.query(User).join(Address, Address.user_id == User.id)
            .filter(exists().where(
                and_(Address.email_address.like('%sqlalchemy%'), Address.user_id == User.id)
            )).all())

def fix_error():
    # The answer: https://stackoverflow.com/questions/35690518/sqlalchemy-query-filter-returned-no-from-clauses-due-to-auto-correlation
    from sqlalchemy import exists, and_
    from sqlalchemy.orm import aliased

    aliasedAddr = aliased(Address)
    print(session.query(User).join(Address, Address.user_id == User.id)
            .filter(exists().where(
                and_(aliasedAddr.email_address.like('%sqlalchemy%'), aliasedAddr.user_id == User.id)
            )).all())

if __name__ == "__main__":
    try:
        raise_error()
    except Exception as e:
        print(e)
        fix_error()
```
## 说明
执行raise_error函数会报错
> sqlalchemy.exc.InvalidRequestError: Select statement '<sqlalchemy.sql.selectable.Select object at 0x7f16eb0989a0>' returned no FROM clauses due to auto-correlation; specify correlate(<tables>) to control correlation manually. 

## 解释
```
实际上exist语句是一个子查询(subquery), 在subquery中不允许重复查询主查询中存在的表(Calling the same table twice (FROM Revision) in the same query is not allowed unless you use an alias.)
```
