"""Collections of various Dhivehi texts.

    އެކި ބާވަތުގެ ދިވެހި ލިޔުންތައް
"""

from dhivehi_nlp._helpers import _db_connect


def _db_read(name: str) -> str:
    con = _db_connect()
    cursor = con.cursor()
    query = f"SELECT content FROM corpus WHERE name='{name}'"
    cursor.execute(query)
    content = cursor.fetchone()
    con.close()
    return content[0]


def news() -> str:
    """News article from sun.mv https://sun.mv/145845

    ސަން އެމްވީގެ ނޫސް ހަބަރެއް
    """
    return _db_read("news")


def story() -> str:
    """Rehendhi short story by Aishath Afra https://vaahaka.com/story/9604/

    އައިޝަތު އަފްރާގެ ކުރުވާހަކަ ރެހެނދި
    """
    return _db_read("story")


def tweet() -> str:
    """Tweet by @FSaaira https://twitter.com/FSaaira/status/1334579523006812160

    ފާތުމަތު ސާއިރާގެ ޓްވީޓެއް
    """
    return _db_read("tweet")


def lyrics() -> str:
    """Lyrics of Hingaa Hoadhama Hey by Hussain Ali

    ހުސެން އަލީގެ ހިނގާ ހޯދަމާހޭ ލަވައިގެ ޅެން
    """
    return _db_read("lyrics")


def textbook() -> str:
    """Excerpt from Dhivehi 3 (Sh) teachers book
    https://www.moe.gov.mv/en/category/view/31

    ދިވެހި 3 (ށ) މުދައްރިސުންގެ ފޮތުން ތަންކޮޅެއް
    """
    return _db_read("textbook")
