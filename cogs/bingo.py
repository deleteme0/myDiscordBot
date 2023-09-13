#6/8/2020
import discord
from discord.ext import commands
import random
import time

from discord.ext.commands import Bot

bingo_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]


async def display_board_to_dms(ctx, whole_board, player_no, players):

    list = check(whole_board, player_no)

    for i in range(player_no):
        style_1 = ""
        if list[i] == 0:
            await players[i].send(embed=discord.Embed(title="B    I    N    G    O"))
        elif list[i] == 1:
            await players[i].send(embed=discord.Embed(title="X    I    N    G    O"))
        elif list[i] == 2:
            await players[i].send(embed=discord.Embed(title="X    X    N    G    O"))
        elif list[i] == 3:
            await players[i].send(embed=discord.Embed(title="X    X    X    G    O"))
        elif list[i] == 4:
            await players[i].send(embed=discord.Embed(title="X    X    X    X    O"))
        elif list[i] == 5:
            await players[i].send(embed=discord.Embed(title="X    X    X    X    X"))

        for row in range(0, 5):

            printing = []
            for coloumn in range(0, 5):
                if whole_board[i][row][coloumn][1] == 1:
                    printing.append("X  ")

                else:
                    a = whole_board[i][row][coloumn][0]
                    if len(str(a)) == 1:
                        printing.append(str(a) + "  ")
                    else:
                        printing.append(a)
            full_print = ""
            for x in printing:
                full_print = full_print + str(x)
                full_print = full_print + "       "
            style_1 = style_1 + full_print + "\n"
        #print(style_1)
        await players[i].send(style_1)


def horizontal_check(board):
    finish = 0
    for row in range(0, 5):
        count = 0
        for coloumn in range(0, 5):

            if board[row][coloumn][1] == 1:
                count = count + 1
        if count == 5:
            finish = finish + 1
    return int(finish)


def vertical_check(board):
    finish = 0
    for coloumn in range(0, 5):
        count = 0
        for row in range(0, 5):
            if board[row][coloumn][1] == 1:
                count = count + 1
        if count == 5:
            finish = finish + 1
    return int(finish)


def diagonal_check(board):
    finish = 0
    count = 0

    for r_c in range(0, 5):
        if board[r_c][r_c][1] == 1:
            count = count + 1
    if count == 5:
        finish = finish + 1

    count = 0
    coloumn = 0
    for row in range(4, -1, -1):
        if board[row][coloumn][1] == 1:
            count = count + 1
        coloumn = coloumn + 1
    if count == 5:
        finish = finish + 1

    return finish


def check(all_board, player_no):
    total_finishes = []
    for i in range(player_no):
        total_finish = vertical_check(all_board[i]) + horizontal_check(all_board[i]) + diagonal_check(all_board[i])
        total_finishes.append(total_finish)
        print(total_finishes)

    return total_finishes


def bingo_check(all_board, player_no):

    bingo_no = 10
    list = check(all_board, player_no)
    no = 0
    for i in list:
        if int(i) == 5:
            bingo_no = no
            break

        no = no + 1
    return bingo_no


def board_gen():
    board = [[[[], []], [[], []], [[], []], [[], []], [[], []]], [[[], []], [[], []], [[], []], [[], []], [[], []]],
             [[[], []], [[], []], [[], []], [[], []], [[], []]], [[[], []], [[], []], [[], []], [[], []], [[], []]],
             [[[], []], [[], []], [[], []], [[], []], [[], []]]]
    for row in range(0, 5):
        for coloumn in range(0, 5):
            # noinspection PyTypeChecker
            board[row][coloumn][1] = 0
    no = 0
    order = 0
    random.shuffle(bingo_numbers)
    for row in range(0, 5):
        for coloumn in range(0, 5):
            board[row][coloumn][no] = bingo_numbers[order]
            order = order + 1
    #print(board)
    return board


def cross_no(number, number_of_boards, boards):
    for row in range(0, 5):
        for coloumn in range(0, 5):
            for board_no in range(0, number_of_boards):
                if boards[board_no][row][coloumn][0] == number:
                    boards[board_no][row][coloumn][1] = 1


def print_board(board):
    for row in board:
        for coloumn in row:
            pass
            #print(coloumn[0], end='    ')
        #print()


async def dm_users(ctx, users, whole_board):
    for i in range(len(whole_board)):
        await users[i].send(whole_board[i])


class bingo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('LET THE GAMES BEGIN!!')

    @commands.command()
    async def start_bingo(self, ctx):

        whole_board = []

        def check1(m):
            return m.channel == ctx.channel and m.author != Bot.user

        game = True
        run = True
        a = 0
        players = []

        await ctx.send(f"type JOIN to join the game")
        await ctx.send("type play to start the game after everyone typed JOIN")

        while run:

            msg = await self.bot.wait_for('message', check=check1)
            
            time.sleep(1)
            a = a + 1
            if msg.content in ['play', 'PLAY', 'start', "START"]:

                run = False

            else:
                if msg.content == 'JOIN':
                    await ctx.send(f"{msg.author.mention} has joined ")
                    players.append(msg.author)
        await ctx.send("The participating users are:")

        player_no = len(players)
        for i in range(player_no):
            sub_board = board_gen()
            whole_board.append(sub_board)

        for i in range(len(players)):
            print(players[i].mention )
            await ctx.send(f"{players[i].mention}")

        chance = 0
        round_no = 0

        await ctx.send("LET THE GAME BEGIN")
        while game:     # main game loop

            if round_no == 0:
                await display_board_to_dms(ctx, whole_board, player_no, players)
                round_no = round_no + 1

            await ctx.send(f"{players[chance].mention} \'s turn")
            no_chosen = await self.bot.wait_for('message', check=lambda message: message.author == players[chance])

            if int(no_chosen.content) not in bingo_numbers and no_chosen.content not in ["end"]:
                await ctx.send("pls enter a valid number")

            else:
                if chance == (int(player_no) - 1):
                    chance = 0
                else:
                    chance = chance + 1

            if no_chosen.content == 'end':
                await ctx.send(f"The game was ended by {players[chance].mention}")
                break

            cross_no(int(no_chosen.content), player_no, whole_board)
            await display_board_to_dms(ctx, whole_board, player_no, players)
            done = bingo_check(whole_board, player_no)

            if done != 10:
                game = False
                winner = done
                await ctx.send(f"GGs THE WINNER IS {players[winner].mention}")
                await ctx.send("ty for playing :)")
                await players[winner].send("YOU WON!!!") 


def setup(Bot):
    Bot.add_cog(bingo(Bot))
