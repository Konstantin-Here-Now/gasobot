import logging

from telegram import Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler, MessageHandler, filters,
)

from commands.first_stage_commands import start, about_company, production_level, options
from commands.other_commands import callback_not_realized_yet, unknown_command
from commands.second_stage_commands import orders, become_partner, check_contract
from settings import TOKEN, FIRST_STATE, SECOND_STATE, THIRD_STATE

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the bot."""
    application = Application.builder().token(TOKEN).build()

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            FIRST_STATE: [
                CallbackQueryHandler(orders, pattern="^" + "orders" + "$"),
                CallbackQueryHandler(about_company, pattern="^" + "about_company" + "$"),
                CallbackQueryHandler(production_level, pattern="^" + "production_level" + "$"),
            ],
            SECOND_STATE: [
                CallbackQueryHandler(become_partner, pattern="^" + "become_partner" + "$"),
                CallbackQueryHandler(check_contract, pattern="^" + "check_contract" + "$"),
            ],
            THIRD_STATE: [
                # not realized
                CallbackQueryHandler(callback_not_realized_yet)
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT or (~filters.COMMAND), unknown_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
