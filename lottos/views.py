from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request, 'lottos/index.html')

def basic_lotto_page(request):
    lotto_nums = []
    for i in range(0,6):
        lotto_nums.append(random.randrange(1,46))
    print(lotto_nums)
    return render(request, 'lottos/basic_lotto.html', {"lotto_nums":lotto_nums})

def challenge_lotto_input(request):
    return render(request, 'lottos/challenge_lotto_input.html')

def challenge_lotto_output(request):
    game = int(request.GET.get('game'))
    lottos = []
    for i in range(game):
        lotto_nums = []
        for j in range(0,6):
            lotto_nums.append(random.randrange(1,46))
        lottos.append(lotto_nums)
    return render(request, 'lottos/challenge_lotto_output.html', {'game':game, 'lottos':lottos})