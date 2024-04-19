from fastapi.responses import FileResponse

from config import const


async def favicon() -> FileResponse:
    """Favicon file.

    Returns:
        FileResponse with favicon
    """
    return FileResponse(const.STATIC_PATH / 'favicon.ico')
