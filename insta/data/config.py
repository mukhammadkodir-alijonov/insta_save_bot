from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = ${{secrets.TOKEN}}  # Bot toekn
ADMINS = [1755665750]  # adminlar ro'yxati

