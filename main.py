import nextcord, json
from nextcord.ext import commands

with open("config.json", "r") as file:
    ConfigData = json.load(file)

client = commands.Bot(case_insensitive = True, command_prefix = ConfigData["prefix"], intents = nextcord.Intents.all(), allowed_mentions = nextcord.AllowedMentions(everyone = False, replied_user = True, roles = False, users = False))
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{client.user.name}#{client.user.discriminator}")


@client.command()
async def aprobar(ctx, member: nextcord.Member):
    if ctx.author.guild_permissions.manage_roles:
        role = nextcord.utils.get(member.guild.roles, id=898716040547143740)
        if role in member.roles:
            await member.remove_roles(role)
            role = nextcord.utils.get(member.guild.roles, id=1046797696989659186)
            await member.add_roles(role)
            channel = nextcord.utils.get(member.guild.text_channels, id=1046805478237290576)
            await channel.send(f"<@&975073900343984138> <@!{member.id}> pasa por <#856620171631132702> y no se te olvide leer <#888120313479589898> y <#881476832376004608> Y hecha un vistazo en <#954526605340991508> Tambien si gustas puedes presentarte en <#881467745328308225> Si tienes algun problema o queja o sugerencia tienes <#856593336869191680> o <#963852674581807114>.")
        else:
            role = nextcord.utils.get(member.guild.roles, id=1046797696989659186)
            if role in member.roles:
                await ctx.send(f"{member.mention} ya esta verificado.")
            else:
                await ctx.send(f"{member.mention} no tiene el rol no verificado.")
    else:
        await ctx.send(f"<@!{ctx.author.id}> No tienes permisos para ejecutar este comando.")

@client.command()
async def approve(ctx, member: nextcord.Member):
    if ctx.author.guild_permissions.manage_roles:
        role = nextcord.utils.get(member.guild.roles, id=898716040547143740)
        if role in member.roles:
            await member.remove_roles(role)
            role = nextcord.utils.get(member.guild.roles, id=1046797696989659186)
            await member.add_roles(role)
            channel = nextcord.utils.get(member.guild.text_channels, id=1046805478237290576)
            await ctx.reply(f"<@!{member.id}> verificado.", )
            await channel.send(f"<@&975073900343984138>  Pass through <#856620171631132702>  and do not forget to read <#888120313479589898> or <#1022293946170347602>  and <#954526605340991508> , <#1024065194399383595>   or suggestion you have<#856593336869191680> or<#963852674581807114>. If you only talk english you need a **@ Ingles / English**, react in <#856620171631132702>")
        else:
            role = nextcord.utils.get(member.guild.roles, id=1046797696989659186)
            if role in member.roles:
                await ctx.send(f"{member.mention} ya esta verificado.")
            else:
                await ctx.send(f"{member.mention} no tiene el rol no verificado.")
    else:
        await ctx.send(f"<@!{ctx.author.id}> no tienes permisos para ejecutar este comando.")

client.run(ConfigData["token"])