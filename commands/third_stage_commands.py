# pylint: disable=unused-argument

from telegram import Update
from telegram.ext import ContextTypes

from commands.other_commands import callback_not_realized_yet
from keyboards import THIRD_STATE_KEYBOARD
from settings import THIRD_STATE, CHECK_CONTRACT_TEXT


async def check_contract(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    reply_markup = THIRD_STATE_KEYBOARD
    await query.message.reply_text(
        text=CHECK_CONTRACT_TEXT, reply_markup=reply_markup
    )
    return THIRD_STATE


async def change_contract(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await callback_not_realized_yet(update, context)


async def terminate_contract(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await callback_not_realized_yet(update, context)
