# Generated by Django 3.0.8 on 2020-07-14 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_type', models.CharField(max_length=100)),
                ('Full_names', models.CharField(max_length=100)),
                ('Surname', models.CharField(max_length=100)),
                ('Not_Registered', models.CharField(max_length=100)),
                ('Informal', models.CharField(max_length=100)),
                ('Registration_no', models.IntegerField()),
                ('Indian', models.CharField(max_length=100)),
                ('Disability', models.CharField(max_length=100)),
                ('If_Yes_please_elaborate', models.CharField(max_length=100)),
                ('Transport_Required', models.CharField(max_length=100)),
                ('If_Yes_please_feel_in_pick_up_address', models.CharField(max_length=100)),
                ('Next_to', models.CharField(max_length=100)),
                ('Are_you_bringing_guest', models.CharField(max_length=100)),
                ('Yes', models.CharField(max_length=100)),
                ('No', models.CharField(max_length=100)),
                ('Guests_details', models.CharField(max_length=1000)),
                ('Special_requests', models.CharField(max_length=1000)),
                ('ADMINISTRATION_PAGE', models.CharField(max_length=1000)),
                ('Event_Details', models.CharField(max_length=1000)),
                ('Event_Name', models.CharField(max_length=1000)),
                ('Date', models.DateField()),
                ('Event_Duration', models.IntegerField()),
                ('Time', models.TimeField(auto_now_add=True)),
                ('Perpose_of_the_event', models.CharField(max_length=1000)),
                ('Admin_Details', models.CharField(max_length=1000)),
                ('Mr', models.CharField(max_length=1000)),
                ('Mrs', models.CharField(max_length=1000)),
                ('Ms', models.CharField(max_length=1000)),
                ('Male', models.CharField(max_length=1000)),
                ('Female', models.CharField(max_length=1000)),
                ('Black', models.CharField(max_length=1000)),
                ('White', models.CharField(max_length=1000)),
                ('Coloured', models.CharField(max_length=1000)),
                ('Known_as', models.CharField(max_length=1000)),
                ('Identity_number', models.IntegerField()),
                ('Position', models.CharField(max_length=1000)),
                ('Nationality', models.CharField(max_length=1000)),
                ('Race', models.CharField(max_length=1000)),
                ('Organasing_Body', models.CharField(max_length=1000)),
                ('CEO', models.CharField(max_length=1000)),
                ('Email_Address', models.EmailField(max_length=254)),
                ('Host', models.CharField(max_length=1000)),
                ('Contact_Person', models.CharField(max_length=1000)),
                ('Cell', models.IntegerField()),
                ('Alt_numnber', models.IntegerField()),
                ('Fax_number', models.IntegerField()),
                ('Physical_Address', models.CharField(max_length=1000)),
                ('Line_01', models.CharField(max_length=1000)),
                ('Line_02', models.CharField(max_length=1000)),
                ('Suburb_Township', models.CharField(max_length=1000)),
                ('City', models.CharField(max_length=1000)),
                ('Manucipality', models.CharField(max_length=1000)),
                ('Province', models.CharField(max_length=1000)),
                ('Code', models.IntegerField()),
                ('Stack_Holders', models.CharField(max_length=1000)),
                ('Company_Name', models.CharField(max_length=1000)),
                ('Attendance_Confirmed', models.CharField(max_length=1000)),
                ('Import', models.CharField(max_length=1000)),
                ('export', models.CharField(max_length=1000)),
                ('upload', models.FileField(upload_to='uploads/')),
                ('img', models.ImageField(upload_to='PICTURES')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('Username', models.CharField(max_length=1000)),
                ('Password', models.CharField(max_length=1000)),
                ('Conform_Password', models.CharField(max_length=1000)),
                ('Old_Password', models.CharField(max_length=1000)),
                ('New_Password', models.CharField(max_length=1000)),
            ],
        ),
    ]
