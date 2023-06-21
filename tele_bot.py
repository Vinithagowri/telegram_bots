import telegram.ext
token="*****"
updater=telegram.ext.Updater("6001148446:****",use_context=True)
dispatcher=updater.dispatcher

def help(update,context):
    update.message.reply_text(
        """
        /start -> To know about me... \n
        /my_fav ->To know about my favorite things \n
        /my_hab ->To know about my daily habits \n
        /want_DM -> To Direct message me\n
        /my_yt -> visit my youtube channal\n
        /contact_me -> to contack me\n
        /help -> For these options \n
        """
    )
def start(update,context):
    update.message.reply_text(" Hello Buddies!!! I am vineeeta from india \n\
I am a under graduate student in CSE... \n I am here to chat with you \n so feel free...Lets chat \n click here.. /help")
def my_fav(update,context):
    update.message.reply_text(" Now I am going to share about some of my favorite things in this little world!! \
    \n\nApart From the world I love to watch the night sky with moons and stars \
    \n\nI love the amazing environment that this nature develpes Every things in this world is beautiful \
    \n\nI like the books which gives us wisdom and courage \
    \n\nAnd the one who search for new things ....Ya..that's you.... ")
def my_hab(update,context):
    update.message.reply_text("Are you eagar to know about my habits... \
    \n Here is it is \
    \n 1.reading myself \
    \n 2.reading books of wise menss\n 3.self complacement of myself \
    \n 4.listening lite music and many more")
def want_DM(update,context):
    update.message.reply_text("what to chat with me search fo this user id ---vineeta_1970")
def my_yt(update,context):
    update.message.reply_text(" To support me visit this YouTube channal -- https://www.bing.com/ck/a?!&&p=13f9a3459d7dd118JmltdHM9MTY4MDkxMjAwMCZpZ3VpZD0zODE0NGZjYS03NWUzLTYzNzUtM2YyMi01ZmYzNzQ0ZTYyYmYmaW5zaWQ9NTIwMw&ptn=3&hsh=3&fclid=38144fca-75e3-6375-3f22-5ff3744e62bf&psq=mr+gk+tamil&u=a1aHR0cHM6Ly93d3cueW91dHViZS5jb20vYy9NckdLVGFtaWwvdmlkZW9z&ntb=1")
def contact_me(update,context):
    update.message.reply_text("Contact me at instagram at vineeta_vini_1970")
dispatcher.add_handler(telegram.ext.CommandHandler("start",start))
dispatcher.add_handler(telegram.ext.CommandHandler("my_fav",my_fav))
dispatcher.add_handler(telegram.ext.CommandHandler("my_hab",my_hab))
dispatcher.add_handler(telegram.ext.CommandHandler("want_DM",want_DM))
dispatcher.add_handler(telegram.ext.CommandHandler("my_yt",my_yt))
dispatcher.add_handler(telegram.ext.CommandHandler("contact_me",contact_me))
dispatcher.add_handler(telegram.ext.CommandHandler("help",help))
updater.start_polling()
updater.idle()
