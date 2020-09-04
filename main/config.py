import sys
sys.path.append('../splatoon2_bot_core/')
from translation import CN_LEAGUE, CN_RANKED, CN_REGULAR, CN_SALMON_RUN

CMD_QR = True

KEYWORDS_LEAGUE = [CN_LEAGUE, "双排", "四排", "排排", "pp","pppp", "wyx", "陪练"]
KEYWORDS_RANKED = [CN_RANKED, "真格", "伤身体", "自闭"]
KEYWORDS_REGULAR = [CN_REGULAR, "涂地", "常规"]
KEYWORDS_SALMON_RUN = [CN_SALMON_RUN, "dg", "工"]
KEYWORDS_RANDOM = ["随机",'祭典']

UNKNOWN_MSG = "查询格式:\n" \
              "- 查询 (当前/下个/下下...个/X小时后) 全部/组排/单排/涂地/打工\n" \
              "- 查询（祭典）随机 [用来随机武器私房]\n" \
              "- 查询（祭典）随机+数字或字母密码 [多个群用来随机武器私房，有效期100秒]"

LOG_FILE = "splatoon2_bot_core.log"
