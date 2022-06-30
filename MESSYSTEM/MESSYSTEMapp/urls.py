from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('Login/', views.signin, name='Login'),
    #admin
    path('Register/', views.register, name='Register'),
    path('Admin_Distribution/', views.adminFAD, name='Admin_Distribution'),
    path('Admin_Distribution_Pdf/', views.pdf_distribution, name='Admin_Distribution_Pdf'),
    path('Admin_Financial_Assistance/', views.adminFA, name='Admin_Financial_Assistance'),
    path('Admin_Financial_Assistance_Pdf/', views.pdf_assistance, name='Admin_Financial_Assistance_Pdf'),
    path('AdminFAD_Delete/<str:lrn_scholarship>', views.AdminFAD_Delete, name='AdminFAD_Delete'),
    path('AdminFAD_Update/<str:lrn_scholarship>', views.AdminFAD_Update, name='AdminFAD_Update'),
    path('Admin_Homepage/', views.adminhomepage, name='Admin_Homepage'),
    path('Student_Transaction/', views.student_transaction, name='Student_Transaction'),
    path('Student_Transaction_Pdf/', views.pdf_student_transaction, name='Student_Transaction_Pdf'),
    #student
    path('Student_History_Transaction/<str:username>', views.student_history_transaction, name='Student_History_Transaction'),
    #teacher
    path('Teacher_Transaction/', views.teacher_transaction, name='Teacher_Transaction'),
    path('Teacher_Transaction_Pdf/', views.pdf_teacher_transaction, name='Teacher_Transaction_Pdf'),
    path('Teacher_Transaction_Delete/<str:lrn_student>', views.teacher_transaction_delete, name='Teacher_Transaction_Delete'),
    path('Teacher_Transaction_Update/<str:lrn_student>', views.teacher_transaction_update, name='Teacher_Transaction_Update'),
    path('Distribution_and_Retrieval/<str:lrn_student>', views.distribution_and_retrieval, name='Distribution_and_Retrieval'),
    path('Logout/', views.logout_view, name='Logout'),
]