from _asyncio import Task
from typing import Any


from asyncio.events import AbstractEventLoop


import os
import glob
import asyncio
import logging
from functools import partial

path: str = os.path.join(os.getcwd(), "zone_cleanup.log")
if os.path.isfile(path):
    if os.path.getsize(path) > 0:
        os.remove(path)

logging.basicConfig(
    filename="zone_cleanup.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def async_remove(path) -> bool:
    loop: AbstractEventLoop   = asyncio.get_running_loop()
    try:
        await loop.run_in_executor(None, partial(os.remove, path))
        logging.info(f"Removido: {path}")
        return True
    except Exception as e:
        logging.error(f"Erro ao remover {path}: {e}")
        return False


async def remove_zone_files(dir_path) -> None:
    patterns:list[str] = [
        os.path.join(dir_path, "*:Zone.Identifier"),
        os.path.join(dir_path, ".*:Zone.Identifier")
    ]

    tasks: list = []
    for pattern in patterns:
        for path in glob.glob(pattern):
            tasks.append(asyncio.create_task(async_remove(path)))

    if tasks:
        results: list = await asyncio.gather(*tasks)
        total: int = sum(results)
        logging.info(f"Total removido em {dir_path}: {total}")


async def explore_directories(start_dir) -> None:
    logging.info(f"Iniciando varredura async em: {start_dir}")

    tasks: list = []
    for root, _, _ in os.walk(start_dir):
        logging.info(f"Entrando no diretório: {root}")
        tasks.append(asyncio.create_task(remove_zone_files(root)))

    if tasks:
        await asyncio.gather(*tasks)

async def explore_multiple(dirs:list) -> None:
    tasks: list[Task[None]] = [asyncio.create_task(explore_directories(d)) for d in dirs]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
   
    logging.info("Script de limpeza de Zone.Identifier iniciado.")
    
    try:
        listDirectory: list[str] = [
            os.getcwd(),
        ]

        asyncio.run(explore_multiple(listDirectory))
    except Exception as e:
        logging.error(f"Erro ao executar script: {e}")
    finally:
        logging.info("Script finalizado.")
        with open(path, "r") as f:
            print(f.read())
            
