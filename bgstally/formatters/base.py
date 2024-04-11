from bgstally.activity import Activity
from bgstally.constants import DiscordActivity, FormatMode
from bgstally.state import State
from bgstally.utils import _


class BaseFormatterInterface:
    """The base interface for discord formatters
    """

    def __init__(self, state: State):
        """Instantiate class

        Args:
            state (State): The State object containing persistent values and settings
        """
        self.state: State = state


    def get_name(self) -> str:
        """Get the name of this formatter

        Returns:
            str: The name of this formatter for choosing in the UI
        """
        pass


    def get_mode(self) -> FormatMode:
        """Get the output format mode that this Formatter supports

        Returns:
            FormatMode: The supported format mode
        """
        pass


class TextFormatterInterface(BaseFormatterInterface):
    """A Discord formatter that returns plain text
    """

    def get_text(self, activity: Activity, activity_mode: DiscordActivity, discord: bool = False, system_names: list = None, lang: str = None) -> str:
        """Generate formatted text for a given instance of Activity

        Args:
            activity (Activity): The Activity object containing the activity to post
            activity_mode (DiscordActivity): Determines the type(s) of activity to post
            discord (bool, optional): True if the destination is Discord (so can include Discord-specific formatting such
            as ```ansi blocks and UTF8 emoji characters), False if not. Defaults to False.
            system_names (list, optional): A list of system names to restrict the output for. Defaults to None.
            lang (str, optional): The language code for this post. Defaults to None.

        Returns:
            str: The output text
        """
        pass


class FieldFormatterInterface(BaseFormatterInterface):
    """A Discord formatter that returns fields for displaying in a Discord embed
    """

    def get_fields(self, activity: Activity, activity_mode: DiscordActivity, discord: bool = False, system_names: list = None, lang: str = None) -> list[dict]:
        """Generate a list of discord embed fields, conforming to the embed field spec defined here:
        https://birdie0.github.io/discord-webhooks-guide/structure/embed/fields.html - i.e. each field should be a dict
        containing 'name' and 'value' str keys, and optionally an 'inline' bool key

        Args:
            activity (Activity): The Activity object containing the activity to post
            activity_mode (DiscordActivity): Determines the type(s) of activity to post
            system_names (list, optional): A list of system names to restrict the output for. Defaults to None.
            lang (str, optional): The language code for this post. Defaults to None.

        Returns:
            list[dict]: A list of dicts, each containing an embed field containing 'name' and 'value' str keys, and optionally an 'inline' bool key
        """
        pass
