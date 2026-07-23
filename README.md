# Academic Notes Organizer

یک سیستم مدیریت جزوات و اشتراک‌گذاری آموزشی با قابلیت‌های فروشگاهی (نمایشی) و اجتماعی.

---

## درباره‌ی پروژه

این پروژه یک وب‌اپلیکیشن است که به کاربران اجازه می‌دهد:
- ثبت‌نام، ورود و خروج
- ایجاد، ویرایش و حذف درس‌ها
- ایجاد، ویرایش و حذف جزوه‌ها (همراه با آپلود فایل)
- آپلود هر نوع فایل (PDF، Word، Python، عکس، و ...)
- جستجوی متنی در عنوان و محتوای جزوه‌ها (با پشتیبانی از مارک‌داون)
- فیلتر جزوه‌ها بر اساس برچسب (امتحان، تمرین، پروژه، جزوه)
- نمایش درس‌ها به صورت ساختار درختی (File Explorer)
- مشاهده‌ی پروفایل عمومی کاربران و یک داشبورد شخصی برای هر کاربر که اطلاعات زمان آپلود هر فایل را مشخص می‌کند و تعداد درسها و تعداد جزوات را نشان می‌دهد 
- قسمتی برای مشاهده و اشتراک‌گذاری جزوات به صورت عمومی (با قابلیت انتخاب عمومی/خصوصی برای هر درس)
- خرید نمایشی جزوه‌های پولی (انتخاب رایگان / پولی برای هر جزوه)
- امتیازدهی (۱ تا ۵ ستاره) به جزوه‌های عمومی
- کامنت‌گذاری روی جزوه‌های عمومی
- ویرایشگر مارک‌داون برای نوشتن جزوه‌ها
- داشبورد کاربری با نمایش آمار و آخرین فعالیت‌ها
- تست‌نویسی با Django TestCase
- اجرا در محیط لینوکس (Debian)
- کانتینرایزیشن با Docker و Docker Compose

---

## ویرایشگر مارک‌داون

کاربران می‌توانند جزوه‌های خود را با استفاده از ویرایشگر مارک‌داون بنویسند. محتوای نوشته‌شده به‌صورت خودکار به HTML تبدیل شده و در صفحه‌ی نمایش جزوه به‌درستی قالب‌بندی می‌شود.

پشتیبانی از:
- تیترها (`#`, `##`, `###`)
- متن پررنگ (`**`), کج (`*`)
- لیست‌ها (ترتیبی و غیرترتیبی)
- لینک و تصویر
- کد و بلوک‌های کد با هایلایت

---

## تکنولوژی‌ها و کتابخونه‌ها

| ابزار | کاربرد |
|-------|--------|
| Django 6.0.6 | فریم‌ورک اصلی وب |
| SQLite | دیتابیس پیش‌فرض (محلی) |
| Python 3.13 | زبان برنامه‌نویسی |
| HTML/CSS | رابط کاربری (با ریسپانسیو) |
| Docker / Docker Compose | کانتینرایزیشن و اجرای آسان |
| django-markdownx | ویرایشگر مارک‌داون |
| Git | کنترل نسخه و همکاری تیمی |
| Django TestCase | تست‌نویسی |

---

##  ساختار اصلی پروژه

```

academic-notes/
├── config/
│   ├── settings.py
│   └── urls.py
├── notes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── tests.py
│   └── migrations/
├── templates/
│   └── notes/
│       ├── course_list.html
│       ├── note_list.html
│       ├── course_form.html
│       ├── note_form.html
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       ├── public_profile.html
│       ├── public_notes_list.html
│       ├── public_note_create.html
│       ├── purchase.html
│       ├── purchase_success.html
│       └── error.html
├── static/
│   └── css/
│       └── style.css
├── media/
│   └── notes/files/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore

```

---

## راه‌اندازی و اجرا

###  اجرا در ویندوز (محلی)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

 اجرا در لینوکس (Debian)

```bash
cd ~/Desktop/academic-notes
git pull
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

برای اجرا روی شبکه:

```bash
python manage.py runserver 0.0.0.0:8000
```

---

 اجرا با Docker

```bash
docker compose up --build
```

سپس در مرورگر: http://localhost:8000

---

 Docker Volume برای فایل‌های آپلودی

در فایل docker-compose.yml، پوشه‌ی پروژه و media/ به‌عنوان Volume به کانتینر متصل شده‌اند تا فایل‌های آپلودی پس از ری‌استارت کانتینر از بین نروند:

```yaml
volumes:
  - .:/app
  - ./media:/app/media
```

---

 اجرای تست‌ها

```bash
python manage.py test
```

---

 مدل‌های اصلی

Course

· user:ForeignKey به User
· name: CharField
· created_at: DateTimeField

Note

 course:ForeignKey به Course
 title: CharField
 content: TextField (با پشتیبانی از مارک‌داون)
 file: FileField (آپلود هر نوع فایل)
 tag: CharField با انتخاب‌های:
   exam (امتحان)
   exercise (تمرین)
   project (پروژه)
   lecture (جزوه)  پیش‌فرض
 is_public: BooleanField
 price_type: CharField با انتخاب‌های free, paid
 created_at: DateTimeField

Rating

· note:ForeignKey به Note
· user:ForeignKey به User
· score: IntegerField (۱ تا ۵)
· created_at: DateTimeField
· unique_together = ('note', 'user')

Comment

 note:ForeignKey به Note
 user:ForeignKey به User
 text: TextField
 created_at: DateTimeField

---

 قابلیت‌های امنیتی

 احراز هویت با Django Authentication
 دسترسی به صفحات با @login_required
 فیلتر کردن داده‌ها بر اساس کاربر لاگین‌شده
 مدیریت دسترسی به حذف و ویرایش

---

 نکات مهم برای توسعه‌دهنده‌ی جدید

 برای اجرا ابتدا requirements.txt را نصب کن.
 دیتابیس پیش‌فرض SQLite 
 فایل‌های آپلودی در media/notes/files/ ذخیره می‌شوند
 برای اجرا در لینوکس، از python3 و source venv/bin/activate استفاده کن
 در Docker، از پایتون ۳.۱۳ استفاده شده است.
 برای ویرایش جزوه‌ها، از ویرایشگر مارک‌داون استفاده می‌شود.

---

تیم توسعه

 فاطمه گیلانی – توسعه‌دهنده بک‌اند، معماری، داکر، گیت، تست و مدیریت پروژه
 زکیه موسایی – توسعه‌دهنده فرانت‌اند و UI/UX

---

##  کمک از هوش مصنوعی
**DeepSeek**
در طول توسعه‌ی پروژه به‌عنوان دستیار هوش مصنوعی برای
- رفع خطاها و دیباگ
- مشاوره در طراحی معماری
- پیشنهاد ساختار کد و بهینه‌سازی
- راهنمایی در فرآیند داکرایز کردن و گیت

استفاده شده است این ابزار به تسریع روند توسعه کاهش زمان توقف کمک کرد

## چالش‌ها و تصمیمات کلیدی

- به دلیل محدودیت‌های اینترنت و تحریم‌ها، دیپلوی روی -- با مشکل مواجه شد و به‌طور موقت کنار گذاشته شد
- Render و PythonAnyware--
- PostgreSQL نیز به دلیل وقت‌گیر بودن و نیاز به تنظیمات بیشتر، برای توسعه‌ی آینده نگهداری شد
- برای اجرای پایدار و بدون دردسر، پروژه روی دبیان (لینوکس) با Docker 
- کانتینریزه شد تا
- ا از وابستگی به ویندوز
- جلو گیری بشه  wsl به
- با وجود علاقه به پیاده‌سازی کامل، به دلیل فشار دروس دیگر و زمان محدود، اولویت با 
- ارائه‌ی یک نسخه‌ی کامل و قابل‌قبول بود
- در آینده قابلیت های ذکر شده اضافه خواهد شد


 لایسنس

این پروژه برای درس برنامه‌نویسی پیشرفته طراحی شده است