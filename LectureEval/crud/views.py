from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Lecture, Eval
from .forms import LectureForm, EvalForm
#class 기반 뷰를 위한 module


def LectureList(request):
    lectures = Lecture.objects
    return render(request, 'LectureList.html', {'lectures' : lectures})

def EvalList(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    evals = Eval.objects.filter(lect_id = lect_id).order_by('title')
    keys = {
        'lect' : lect,
        'evals' : evals
    }
    return render(request, 'EvalList.html', keys)


def write(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    return render(request, 'write.html', {'lect' : lect})

def create(request):
    if request.method == "POST":
        a_eval = Eval()
        a_eval.lect = Lecture.objects.get(lectureName = request.POST['lect'])
        a_eval.title = request.POST['title']
        a_eval.pub_date = timezone.datetime.now()
        a_eval.body = request.POST['body']
        a_eval.save()
        return redirect('detail/' + str(a_eval.id))
    else:
        return render(request, 'write.html')


def detail(request, eval_id):
    eval_ = get_object_or_404(Eval, pk = eval_id)
    return render(request, 'EvalDetail.html', {'eval_' : eval_})

def update(request, eval_id):
    edit_eval = get_object_or_404(Eval, pk = eval_id)
    #일단 저장되어있던 내용 불러오기

    #제목, 내용 새로 작성해 제출 버튼 눌렀을 때
    if request.method == "POST":
        edit_eval.title = request.POST['title']
        edit_eval.pub_date = timezone.datetime.now()
        edit_eval.body = request.POST['body']
        edit_eval.save()
        return redirect('/detail/' + str(edit_eval.id))
    #get 방식일 경우 -> 페이지 띄우는 용도
    else:
        return render(request, 'Update.html', {'edit_eval' : edit_eval})

def delete(request, eval_id):
    delete_eval = Eval.objects.get(id = eval_id)
    delete_eval.delete()
    return redirect('lectureList')

def addLecture(request):
    if request.method == "POST":
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lectureList')
    else:
        form = LectureForm()
        return render(request, 'addLecture.html', {'form' : form})


def evalpost(request, lect_id):
    if request.method == "POST":
        evalform = EvalForm(request.POST) #request.POST -> 딕셔너리로 포스트 요청된 데이터를 가지고 있음
        if evalform.is_valid():
            post = evalform.save(commit = False) #post는 Eval 모델 객체!
            post.lect = Lecture.objects.get(id = lect_id)
            post.pub_date = timezone.datetime.now()
            post.save()
            return redirect('/detail/' + str(post.id))
    else:
        evalform = EvalForm()
        return render(request, 'evalPost.html', {'evalform' : evalform})

