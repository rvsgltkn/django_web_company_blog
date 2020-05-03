from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Index,About,Service,Testimonial,Gallery,Contact,Banner
#from .forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.template import RequestContext
from django.utils import translation
# Create your views here.



class LangView(View):
    def get(self,request,lang,page):
        request.session['lang']=lang
        translation.activate(lang)
        request.LANGUAGE_CODE=translation.get_language()
        request.session[translation.LANGUAGE_SESSION_KEY]=lang
        print('page :',page)
        if page is None or '':
            page='index'
        return redirect(page)

class IndexView(View):
    def get(self,request):
        if not request.session.get('lang'):
            request.session['lang']='en'
        index_posts=Index.objects.filter(language__code=request.session['lang'])
        service_posts=Service.objects.filter(language__code=request.session['lang'])
        testimonial_posts = Testimonial.objects.filter(language__code=request.session['lang'])
        gallery_posts=Gallery.objects.filter(language__code=request.session['lang'])
        contact_posts=Contact.objects.filter(language__code=request.session['lang']).first()

        print('session : ', request.session['lang'])
        return render(request,'blog/index.html',
                      {
                          'index_posts':index_posts,
                          'service_posts':service_posts,
                          'testimonial_posts':testimonial_posts,
                          'gallery_posts':gallery_posts,
                          'contact_posts':contact_posts
                      })

class AboutView(View):
    def get(self,request):
        if not request.session.get('lang'):
            request.session['lang'] = 'en'
        banner_image=Banner.objects.filter(page='about').first()
        about_posts=About.objects.filter(language__code=request.session['lang'])
        contact_posts = Contact.objects.filter(language__code=request.session['lang']).first()
        return render(request,'blog/about.html', {'posts':about_posts,'banner_image':banner_image.image_url,'contact_posts':contact_posts})

class ServicesView(View):
    def get(self,request):
        if not request.session.get('lang'):
            request.session['lang'] = 'en'
        pk=request.GET.get('pk')
        banner_image=Banner.objects.filter(page='service').first()
        post_detail = Service.objects.filter(language__code=request.session['lang'], id=pk)
        service_posts = Service.objects.filter(language__code=request.session['lang'])
        contact_posts = Contact.objects.filter(language__code=request.session['lang']).first()
        return render(request,'blog/services.html', {'posts':service_posts,'post_detail':post_detail,'banner_image':banner_image.image_url,'contact_posts':contact_posts})

class IndexDetailView(View):
    def get(self,request):
        if not request.session.get('lang'):
            request.session['lang'] = 'en'
        pk=request.GET.get('pk')
        banner_image=Banner.objects.filter(page='index').first()
        post_detail = Index.objects.filter(language__code=request.session['lang'], id=pk)
        posts = Index.objects.filter(language__code=request.session['lang'])
        contact_posts = Contact.objects.filter(language__code=request.session['lang']).first()
        return render(request,'blog/index_detail.html', {'posts':posts,'post_detail':post_detail,'banner_image':banner_image.image_url,'contact_posts':contact_posts})


class ContactView(View):
    def get(self,request):
        if not request.session.get('lang'):
            request.session['lang'] = 'en'

        banner_image=Banner.objects.filter(page='contact').first()
        posts = Contact.objects.filter(language__code=request.session['lang']).first()
        contact_posts = Contact.objects.filter(language__code=request.session['lang']).first()
        return render(request,'blog/contact.html', {'posts':posts,'banner_image':banner_image.image_url,'contact_posts':contact_posts})

class DefaultView(View):
    def get(self,request):
        return redirect('index')

