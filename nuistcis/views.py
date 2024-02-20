from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import  DepartmentForm, ActivityForm, UserForm, NewsCreateForm
from .models import Department, Activity,Newsimages, News, Note, Programs, Programstype, Aboutus, Websitelogo, Schools, Excellentscholar
from django.forms import  modelformset_factory


AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create_department(request):
    context = link_list()
    if not request.user.is_authenticated:
        return render(request, 'nuistcis/login.html')
    else:
        form = DepartmentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            department = form.save(commit=False)
            department.user = request.user
            department.department_logo = request.FILES['department_logo']
            file_type = department.department_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context['departmet'] = department
                context['form'] = form
                context['error_message'] = 'Image file must be PNG, JPG, or JPEG'
                # context = {
                #     'departmet': department,
                #     'form': form,
                #     'error_message': 'Image file must be PNG, JPG, or JPEG',
                # }
                return render(request, 'nuistcis/create_department.html', context)
            department.save()
            return render(request, 'nuistcis/detail.html', {'department': department})
        context['form']=form
        # context = {
        #     "form": form,
        # }
        return render(request, 'nuistcis/create_department.html', context)


def news_list(request):
    context = link_list()
    news = News.objects.all()

    context['news'] = news

    return render(request, 'nuistcis/news_list.html', context)


def link_list():
    news = News.objects.all()
    departments = Department.objects.all()
    rogramstype = Programstype.objects.all()
    websitelogo = Websitelogo.objects.get(id=1)
    programs = Programs.objects.all()
    aboutus = Aboutus.objects.all()
    scholars = Excellentscholar.objects.all()
    school = Schools.objects.all()

    context = {
        'news': news,
        'departments': departments,
        'programtype': rogramstype,
        'aboutus': aboutus,
        'websitelogo': websitelogo,
        'school': school,
        'scholars': scholars,
        'programs': programs,
    }
    return context


def news_slider(request):
    news = News.objects.all()
    department = Department.objects.all()
    program = Programs.objects.all()
    note = Note.objects.all()
    context = link_list()
    context['note'] = note
    context['program']= program
    # context['news'] = news
    # context = {
    #     'news': news,
    #     'department': department,
    #     'note': note,
    # }
    return render(request, 'nuistcis/news_slider.html', context)


def scholar_detail(request, id):
    scholar = Excellentscholar.objects.filter(id=id)

    context = link_list()
    context['scholar'] = scholar

    return render(request, 'nuistcis/scholar_detail.html', context)


def about_list(request, id):
    aboutus = Aboutus.objects.filter(id=id)

    context = link_list()
    context['aboutus'] = aboutus

    return render(request, 'nuistcis/about_list.html', context)


def school_list(request, id):
    school1 = Schools.objects.filter(id=id)

    context = link_list()
    context['school1'] = school1

    return render(request, 'nuistcis/school.html', context)


def news_slider1(request):
    context = link_list()
    news = News.objects.all()

    context['news']= news

    return render(request, 'nuistcis/news_slider1.html', context)


def programs_list(request):
    # programs = Programs.objects.all()
    rogramstype = Programstype.objects.all()
    context = link_list()

    context['programtype'] = rogramstype
    print(context)
    # context = {
    #     # 'program': programs,
    #     'programtype': rogramstype,
    #
    # }
    return render(request, 'nuistcis/programs.html', context)


def programs_listdetail(request,id):
    # programs = get_object_or_404(Programs, programs_type_id=id)
    # programs = Programs.objects.get(programs_type_id=id)
    # programs = Programs.objects.all(programs_type_id=id)
    programs = Programs.objects.filter(programs_type_id=id)
    context = link_list()
    programstype = Programstype.objects.all()

    context['program'] = programs
    context['programtype'] = programstype
    return render(request, 'nuistcis/programs.html', context)


def news_detail(request, id):
    context = link_list()
    news = get_object_or_404(News, pk=id)

    # news = News.objects.get(id=id)
    context['news'] = news

    return render(request, 'nuistcis/news_detail.html', context)


def news_create(request):
    ImageFormset = modelformset_factory(Newsimages, fields=('news_image',), extra=4)
    context = link_list()
    if request.method == 'POST':
        form = NewsCreateForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid() and formset.is_valid():
            news = form.save(commit=False)
            # news.new_author = request.User
            news.save()

            for f in formset:
                try:
                    # print(f)
                    # https://medium.com/all-about-django/adding-forms-dynamically-to-a-django-formset-375f1090c2b0
                    photo = Newsimages(news=news, news_image=f.cleaned_data['news_image'])
                    photo.save()
                    # return redirect('post_list')
                except Exception as e:
                    break
    else:
        form = NewsCreateForm()
        formset = ImageFormset(queryset=Newsimages.objects.none())
    context['form'] = form
    context['formset'] = formset
    # context = {
    #     'form': form,
    #     'formset': formset,
    #     }
    return render(request, 'nuistcis/news_create.html', context)


def create_activity(request, department_id):
    context = link_list()
    form = ActivityForm(request.POST or None, request.FILES or None)
    department = get_object_or_404(Department, pk=department_id)
    if form.is_valid():
        department_activities = department.activity_set.all()
        for s in department_activities:
            if s.activity_title == form.cleaned_data.get("activity_title"):
                context['department'] = department
                context['form'] = form
                context['error_message']= 'You already added that activity'
                # context = {
                #     'department': department,
                #     'form': form,
                #     'error_message': 'You already added that activity',
                # }
                return render(request, 'nuistcis/create_activity.html', context)
        activity = form.save(commit=False)
        activity.department = department
        activity.audio_file = request.FILES['audio_file']
        file_type = activity.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context['department'] = department
            context['form'] = form
            context['error_message'] = 'Audio file must be WAV, MP3, or OGG'
            # context = {
            #     'department': department,
            #     'form': form,
            #     'error_message': 'Audio file must be WAV, MP3, or OGG',
            # }
            return render(request, 'nuistcis/create_activity.html', context)

        activity.save()
        return render(request, 'nuistcis/detail.html', {'department': department})
    context['department'] = department
    context['form'] = form
    # context = {
    #     'department': department,
    #     'form': form,
    # }
    return render(request, 'nuistcis/create_activity.html', context)


def delete_department(request, department_id):
    department = Department.objects.get(pk=department_id)
    department.delete()
    # departments = Department.objects.filter(user=request.user)
    departments = Department.objects.all()
    return render(request, 'nuistcis/index.html', {'departments': departments})


def delete_activity(request, department_id, activity_id):
    department = get_object_or_404(Department, pk=department_id)
    activity = Activity.objects.get(pk=activity_id)
    activity.delete()
    return render(request, 'nuistcis/detail.html', {'department': department})


def detail(request, department_id):
    context = link_list()
    if not request.user.is_authenticated:
        return render(request, 'nuistcis/login.html')
    else:
        context['user'] = request.user
        context['department'] = get_object_or_404(Department, pk=department_id)
        return render(request, 'nuistcis/detail.html', context)


def favorite(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    try:
        if activity.is_favorite:
            activity.is_favorite = False
        else:
            activity.is_favorite = True
        activity.save()
    except (KeyError, Activity.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorite_department(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    try:
        if department.is_favorite:
            department.is_favorite = False
        else:
            department.is_favorite = True
        department.save()
    except (KeyError, Department.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'nuistcis/login.html')
    else:
        # departments = Department.objects.filter(user=request.user)
        context = link_list()
        departments = Department.objects.all()
        context['activity_results'] = Activity.objects.all()
        activity_results = Activity.objects.all()
        query = request.GET.get("q")
        if query:
            context['departments'] = departments.filter(
                Q(department_title__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
            context['activity_results'] = activity_results.filter(
                Q(activity_title__icontains=query)
            ).distinct()
            return render(request, 'nuistcis/index.html', context)
        else:
            return render(request, 'nuistcis/index.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'nuistcis/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print("this is the user :", user)
        if user is not None:
            print("this is the user :", user)
            if user.is_active:
                login(request, user)
                # departments = Department.objects.filter(user=request.user)
                news = News.objects.all()
                department = Department.objects.all()
                note = Note.objects.all()
                context = link_list()
                context['note'] = note
                # departments = Department.objects.all()
                return render(request, 'nuistcis/news_slider.html', context)
            else:
                return render(request, 'nuistcis/login.html', {'error_message': 'Your account has been disabled'})
        else:
            print("this is the user :", user)
            return render(request, 'nuistcis/login.html', {'error_message': 'Invalid login'})
    return render(request, 'nuistcis/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                departments = Department.objects.filter(user=request.user)
                return render(request, 'nuistcis/index.html', {'departments': departments})
    context = {
        "form": form,
    }
    return render(request, 'nuistcis/register.html', context)


def activities(request, filter_by):
    if not request.user.is_authenticated:
        return render(request, 'nuistcis/login.html')
    else:
        try:
            activity_ids = []
            # for department in Department.objects.filter(user=request.user):
            context = link_list()

            for department in Department.objects.all():
                for activity in department.activity_set.all():
                    activity_ids.append(activity.pk)
            users_activities = Activity.objects.filter(pk__in=activity_ids)
            context['filter_by'] = filter_by
            if filter_by == 'favorites':
                context['users_activities'] = users_activities.filter(is_favorite=True)
                context['activity_list'] = users_activities
                context['filter_by'] = filter_by
        except Department.DoesNotExist:
            users_activities = []
        return render(request, 'nuistcis/activities.html', context
        #               {
        #     'activity_list': users_activities,
        #     'filter_by': filter_by,
        # }
                      )
