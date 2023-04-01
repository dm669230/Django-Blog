from django.shortcuts import render
from datetime import date


all_posts = [
    {
        "slug": "Valley-Adventures",
        "image": "mountains.jpg",
        "author": "Vaibhav Srivastava",
        "date": date(2023, 3, 31),
        "title": "Valley Of Flower Trek",
        "excerpt": "The myriad patches of vivid colors under the watchful eyes of the towering snow-capped Himalayas. Heavenly! Isn't it? ",
        "content": """
          With over 300 species of flora and numerous species of endangered flowers and medicinal plants, the valley is no short of an enchantress perched idyllically to cast a spell on the visitors. Believe us your Valley of flowers trek 2022 will be an experience to remember. But reaching this fairy hinterland of Uttarakhand is no child's play. It is a trek; strenuous and moderate difficulties..

          With over 300 species of flora and numerous species of endangered flowers and medicinal plants, Believe us your Valley of flowers trek 2022 will be an experience to remember. But reaching this fairy hinterland of Uttarakhand is no child's play. It is a trek; strenuous and moderate difficulties..

          With over 300 species of flora and numerous species of endangered flowers and medicinal plants, the valley is no short of an enchantress perched idyllically to cast a spell on the visitors. Believe us your Valley of flowers trek 2022 will be an experience to remember. .
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Vaibhav Srivastava",
        "date": date(2023, 3, 10),
        "title": "I Love Coding!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          My goal is to keep growing and keep learning new things as developer,
            eventually i want to become great personel!.

          My goal is to keep growing and keep learning new things as developer,
            eventually i want to become great personel!.

            My goal is to keep growing and keep learning new things as developer,
            eventually i want to become great personel!
        """
    },
    {
        "slug": "Otaku",
        "image": "death_note.jpg",
        "author": "Vaibhav Srivastava",
        "date": date(2017, 8, 5),
        "title": "Sensei Of My Life !",
        "excerpt": "Anime is the best thing in my life because i found most of the answers of my life's questions",
        "content": """
          I don't exactly remember when I first started watching anime, but it was last year or so and my brother suggested to watch demon slayer because he really loved it and the animations on it are sickkkkk. And couldn't stop watching it since then. also I rly love the fact that every single demon had a depressing and sad past and they just get killed by tanjiro and Nezuko. The next one I watched was spy x family. and Anya is soo tricking cutee aaaoihwrgwirgpehogh.
        """
    }
]

# Create your views here.
def get_date(post):
    return post["date"]

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts= sorted_posts[-3:] #decending order
    return render(request, "blog/index.html",{"posts": latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html",{"posts": all_posts})

def post_details(request,slug):
    identified_post=next(post for post in all_posts if post['slug'] == slug )
    return render(request, "blog/post-detail.html" , {"post": identified_post})