import argparse
import asyncio
from typing import TypedDict

from api.authentication.json_web_token import generate_token
from db import selectors
from db.session import Session


class ScriptParams(TypedDict):
    email: str
    first_name: str
    last_name: str


def parse_args() -> ScriptParams:
    parser = argparse.ArgumentParser(
        description='Script for manual creation of user',
    )

    parser.add_argument('-e', '--email', required=True, type=str)
    parser.add_argument('-f', '--first_name', required=True, type=str)
    parser.add_argument('-l', '--last_name', required=True, type=str)

    args = parser.parse_args()

    return ScriptParams(
        email=args.email,
        first_name=args.first_name,
        last_name=args.last_name,
    )


async def create_user(email: str, first_name: str, last_name: str):
    async with Session() as session:
        return await selectors.user.create(
            session=session,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )


def print_info(user_id: int, token: str) -> None:
    print('User created, id:', user_id)
    print('Auth token generated:', token)


async def main():
    script_args = parse_args()
    user = await create_user(
        email=script_args['email'],
        first_name=script_args['first_name'],
        last_name=script_args['last_name'],
    )
    token_data = generate_token(user=user)
    print_info(user_id=user.id, token=token_data.token)


if __name__ == '__main__':
    asyncio.run(main())
