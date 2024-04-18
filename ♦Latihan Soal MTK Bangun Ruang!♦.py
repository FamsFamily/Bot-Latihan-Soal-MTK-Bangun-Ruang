import discord
from discord.ext import commands
import random
import time
import math

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def halo(ctx):
    await ctx.send(f'''
# Hai! Saya {bot.user}!

## Hal yang bisa saya lakukan:
- **Menampilkan soal tentang luas permukaan bangun ruang. Perintah:**
 - ```$luas_permukaan_bangun_ruang 9```*
- **Menampilkan soal tentang volume bangun ruang. Perintah:**
 - ```$volume_bangun_ruang 9```*
- *Jumlah soal. Ganti dengan jumlah soal yang Anda butuhkan atau mengosongkannya

- _Note: Mohon maaf terkadang ada sedikit kesalahan pada angka desimal._

## GitHub: https://github.com/FamsFamily/Bot-Latihan-Soal-MTK-Bangun-Ruang.git
''')

bangun_ruang = ['kubus', 'balok', 'prisma segitiga', 'prisma segiempat', 'tabung', 'limas segitiga', 'limas segiempat', 'kerucut', 'bola']
rdc = ['r','d']

@bot.command()
async def luas_permukaan_bangun_ruang(ctx, count = 10):
    for i in range(count):
        br = random.choice(bangun_ruang)
        if br == 'kubus':
            s = random.randint(1, 100)
            pert = f'''## Pertanyaan:
    Berapakah luas permukaan kubus diatas yang memiliki data berikut?
    s = {s} cm'''
            j = s*s*6
            jaw = f'''## Jawaban:
    ||{j} cm²||'''
        elif br == 'balok':
            p = random.randint(1, 100)
            l = random.randint(1, 100)
            t = random.randint(1, 100)
            pert = f'''## Pertanyaan:
    Berapakah luas permukaan balok diatas yang memiliki data berikut?
    p = {p} cm
    l = {l} cm
    t = {t} cm'''
            j = 2*((p*l)+(p*t)+(l*t))
            jaw = f'''## Jawaban:
    ||{j} cm²||'''
        elif br == 'prisma segitiga':
            t = random.randint(1, 100)
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            b1 = math.ceil(b*1/3)
            b2 = b - b1
            c = round(((b2**2)+(a**2))**0.5,2)
            e = round(((b1**2)+(a**2))**0.5,2)
            pert = f'''## Pertanyaan:
    Berapakah luas permukaan prisma segitiga diatas yang memiliki data berikut?
    a = {a} cm
    b = {b} cm
    c = {c} cm
    e = {e} cm
    t = {t} cm'''
            j = (2*1/2*a*b) + (b+c+e)*t
            jaw = f'''## Jawaban:
    ||{j} cm²||'''
        elif br == 'prisma segiempat':
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            t = random.randint(1, 100)
            pert = f'''## Pertanyaan:
    Berapakah luas permukaan prisma segiempat diatas yang memiliki data berikut?
    a = {a} cm
    b = {b} cm
    t = {t} cm'''
            j = 2*((a*b)+(a*t)+(b*t))
            jaw = f'''## Jawaban:
    ||{j} cm²||'''
        elif br == 'tabung':
            t = random.randint(1, 100)
            rd = random.choice(rdc)
            if rd == 'r':
                r = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah luas permukaan tabung diatas yang memiliki data berikut?
    r = {r} cm
    t = {t} cm'''
                if r%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                j = 2*phi*r*(r+t)
                jaw = f'''## Jawaban:
    ||{j} cm²||'''
            elif rd == 'd':
                d = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah luas permukaan tabung diatas yang memiliki data berikut?
    d = {d} cm
    t = {t} cm'''
                if d%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                r = d/2
                j = 2*phi*r*(r+t)
                jaw = f'''## Jawaban:
    ||{j} cm²|'''
        elif br == 'limas segitiga':
            t = random.randint(1, 100)
            b = random.randint(1, 100)
            b1 = b/2
            a = round(((b**2)-(b1**2))**0.5,2)
            a1 = round(a*1/3,2)
            c = round(((a1**2)+(t**2))**0.5,2)
            pert = f'''## Pertanyaan:
    Berapakah luas permukaan limas segitiga diatas yang memiliki data berikut?
    a = {a} cm
    b = {b} cm
    c = {c} cm
    t = {t} cm'''
            j = (3*1/2*c*b) + 1/2*a*b
            jaw = f'''## Jawaban:
    ||{j} cm²||'''
        elif br == 'limas segiempat':
            t = random.randint(1, 100)
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            a1 = a/2
            b1 = b/2
            c = round(((b1**2)+(t**2))**0.5,2)
            e = round(((a1**2)+(t**2))**0.5,2)
            pert = f'''## Pertanyaan:
    Berapakah luas permukaan limas segiempat diatas yang memiliki data berikut?
    t = {t} cm
    a = {a} cm
    b = {b} cm
    c = {c} cm
    e = {e} cm'''
            j = (2*1/2*c*a) + (2*1/2*e*b) + a*b
            jaw = f'''## Jawaban:
    ||{j} cm²||'''
        elif br == 'kerucut':
            rd = random.choice(rdc)
            if rd == 'r':
                r = random.randint(1, 100)
                s = round(((r**2)+(t**2))**0.5,2)
                pert = f'''## Pertanyaan:
    Berapakah luas permukaan kerucut diatas yang memiliki data berikut?
    r = {r} cm
    s = {s} cm'''
                if r%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                j = phi*r*(r+s)
                jaw = f'''## Jawaban:
    ||{j} cm²||'''
            elif rd == 'd':
                d = random.randint(1, 100)
                r = d/2
                s = round(((r**2)+(t**2))**0.5,2)
                pert = f'''## Pertanyaan:
    Berapakah luas permukaan kerucut diatas yang memiliki data berikut?
    d = {d} cm
    s = {s} cm'''
                if d%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                j = phi*r*(r+s)
                jaw = f'''## Jawaban:
    ||{j} cm²||'''
        elif br == 'bola':
            rd = random.choice(rdc)
            if rd == 'r':
                r = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah luas permukaan bola diatas yang memiliki data berikut?
    r = {r} cm'''
                if r%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                j = 4*phi*r*r
                jaw = f'''## Jawaban:
    ||{j} cm²||'''
            elif rd == 'd':
                d = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah luas permukaan bola diatas yang memiliki data berikut?
    d = {d} cm'''
                if d%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                r = d/2
                j = 4*phi*r*r
                jaw = f'''## Jawaban:
    ||{j} cm²||'''
        time.sleep(1)
        await ctx.send('-------------------------------------------------------------------------------------------------------')
        with open(br+'.png', 'rb') as f:
            gbr = discord.File(f)
            await ctx.send(file=gbr)
        await ctx.send(pert)
        await ctx.send(jaw)

@bot.command()
async def volume_bangun_ruang(ctx, count = 10):
    for i in range(count):
        br = random.choice(bangun_ruang)
        if br == 'kubus':
            s = random.randint(1, 100)
            pert = f'''## Pertanyaan:
    Berapakah volume kubus diatas yang memiliki data berikut?
    s = {s} cm'''
            j = s*s*s
            jaw = f'''## Jawaban:
    ||{j} cm³||'''
        elif br == 'balok':
            p = random.randint(1, 100)
            l = random.randint(1, 100)
            t = random.randint(1, 100)
            pert = f'''## Pertanyaan:
    Berapakah volume balok diatas yang memiliki data berikut?
    p = {p} cm
    l = {l} cm
    t = {t} cm'''
            j = p*l*t
            jaw = f'''## Jawaban:
    ||{j} cm³||'''
        elif br == 'prisma segitiga':
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            t = random.randint(1, 100)
            pert = f'''## Pertanyaan:
    Berapakah volume prisma segitiga diatas yang memiliki data berikut?
    a = {a} cm
    b = {b} cm
    t = {t} cm'''
            j = 1/2*a*b*t
            jaw = f'''## Jawaban:
    ||{j} cm³||'''
        elif br == 'prisma segiempat':
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            t = random.randint(1, 100)
            pert = f'''## Pertanyaan:
    Berapakah volume prisma segiempat diatas yang memiliki data berikut?
    a = {a} cm
    b = {b} cm
    t = {t} cm'''
            j = a*b*t
            jaw = f'''## Jawaban:
    ||{j} cm³||'''
        elif br == 'tabung':
            t = random.randint(1, 100)
            rd = random.choice(rdc)
            if rd == 'r':
                r = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah volume tabung diatas yang memiliki data berikut?
    r = {r} cm
    t = {t} cm'''
                if r%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                j = phi*r*r*t
                jaw = f'''## Jawaban:
    ||{j} cm³||'''
            elif rd == 'd':
                d = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah volume tabung diatas yang memiliki data berikut?
    d = {d} cm
    t = {t} cm'''
                if d%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                r = d/2
                j = phi*r*r*t
                jaw = f'''## Jawaban:
    ||{j} cm³|'''
        elif br == 'limas segitiga':
            t = random.randint(1, 100)
            b = random.randint(1, 100)
            b1 = b/2
            a = round(((b**2)-(b1**2))**0.5,2)
            pert = f'''## Pertanyaan:
    Berapakah volume limas segitiga diatas yang memiliki data berikut?
    a = {a} cm
    b = {b} cm
    t = {t} cm'''
            j = 1/3*1/2*a*b*t
            jaw = f'''## Jawaban:
    ||{j} cm³||'''
        elif br == 'limas segiempat':
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            t = random.randint(1, 100)
            pert = f'''## Pertanyaan:
    Berapakah volume limas segiempat diatas yang memiliki data berikut?
    a = {a} cm
    b = {b} cm
    t = {t} cm'''
            j = 1/3*a*b*t
            jaw = f'''## Jawaban:
    ||{j} cm³||'''
        elif br == 'kerucut':
            t = random.randint(1, 100)
            rd = random.choice(rdc)
            if rd == 'r':
                r = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah volume kerucut diatas yang memiliki data berikut?
    r = {r} cm
    t = {t} cm'''
                if r%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                j = 1/3*phi*r*r*t
                jaw = f'''## Jawaban:
    ||{j} cm³||'''
            elif rd == 'd':
                d = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah volume kerucut diatas yang memiliki data berikut?
    d = {d} cm
    t = {t} cm'''
                if d%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                r = d/2
                j = 1/3*phi*r*r*t
                jaw = f'''## Jawaban:
    ||{j} cm³||'''
        elif br == 'bola':
            rd = random.choice(rdc)
            if rd == 'r':
                r = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah volume bola diatas yang memiliki data berikut?
    r = {r} cm'''
                if r%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                j = 4/3*phi*r*r*r
                jaw = f'''## Jawaban:
    ||{j} cm³||'''
            elif rd == 'd':
                d = random.randint(1, 100)
                pert = f'''## Pertanyaan:
    Berapakah volume bola diatas yang memiliki data berikut?
    d = {d} cm'''
                if d%7 == 0:
                    phi = 22/7
                else:
                    phi = 3.14
                r = d/2
                j = 4/3*phi*r*r*r
                jaw = f'''## Jawaban:
    ||{j} cm³||'''
        time.sleep(1)
        await ctx.send('-------------------------------------------------------------------------------------------------------')
        with open(br+'.png', 'rb') as f:
            gbr = discord.File(f)
            await ctx.send(file=gbr)
        await ctx.send(pert)
        await ctx.send(jaw)

bot.run("TOKEN RAHASIA ADA DI SINI")
