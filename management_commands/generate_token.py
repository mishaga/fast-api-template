import argparse
import asyncio

from api.authentication.json_web_token import generate_token
from db import selectors
from db.session import Session


def parse_args() -> int:
    parser = argparse.ArgumentParser(
        description='Script for manual generation of a JSON Web Token for a user',
    )

    parser.add_argument('-u', '--user_id', required=True, type=int)

    args = parser.parse_args()

    return args.user_id


async def get_user(user_id: int):
    async with Session() as session:
        return await selectors.user.get(
            session=session,
            user_id=user_id,
        )


def print_info(token: str) -> None:
    print('Auth token generated:', token)


async def main():
    user_id = parse_args()
    user = await get_user(user_id=user_id)
    token_data = generate_token(user=user)
    print_info(token=token_data.token)


if __name__ == '__main__':
    asyncio.run(main())
