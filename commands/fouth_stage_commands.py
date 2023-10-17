# pylint: disable=unused-argument

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from commands.first_stage_commands import options
from commands.third_stage_commands import check_contract
from db.db_connection import view_contract
from exceptions import NotFoundInDatabase
from settings import FOURTH_STATE, LOOK_CONTRACT_TEXT, LOOK_PARTICULAR_CONTRACT_NOT_FOUND_TEXT


async def look_contract(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(text=LOOK_CONTRACT_TEXT)
    return FOURTH_STATE


async def look_particular_contract(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    contract_number = update.message.text
    try:
        contract_info = view_contract(contract_number)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=contract_info)
        return await options(update, context)
    except NotFoundInDatabase:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=LOOK_PARTICULAR_CONTRACT_NOT_FOUND_TEXT)
        return await check_contract(update, context)
