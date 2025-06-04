from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Question, Choice
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import F

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    # context_object_name = "question"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    # context_object_name = "question"

# 투표 처리 로직
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message":"You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))



# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})

# def vote(request, question_id):
#     return HttpResponse(f"You're voting on question {question_id}.")

#     html = """
#     <html>
#     <head>
#         <title>투표 사이트</title>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#                 background-color: #f2f2f2;
#                 padding: 2em;
#             }
#             h1 {color: #333399;}
#             .box {
#                 background: white;
#                 padding: 1.5em;
#                 border-radius: 10px;
#                 box-shadow: 0 0 10px rgba(0,0,0,0.1);
#                 max-width: 600px;
#                 margin: auto;
#             }
#         </style>
#     </head>
#     <body>
#         <div class="box">
#             <h1>안녕하세요!</h1>
#             <p>여기는 <strong>설문조사(polls)</strong> 
#             사이트의 메인 페이지입니다.
#             </p>
#             <p>관리자는 설문을 추가하고, 사용자는 투표할 수 있습니다.</p>
#         </div>
#     </body>
#     </html>
#     """
#     return HttpResponse(html)
# # Create your views here.
