# Generated by Django 4.0.1 on 2022-01-20 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresaColigada', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_endereco', models.CharField(blank=True, choices=[('UNI', 'Único'), ('RES', 'Residencial'), ('COM', 'Comercial'), ('COB', 'Cobrança'), ('ENT', 'Entrega'), ('OUT', 'Outro')], max_length=3, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=16, null=True)),
                ('bairro', models.CharField(blank=True, max_length=64, null=True)),
                ('complemento', models.CharField(blank=True, max_length=64, null=True)),
                ('pais', models.CharField(blank=True, default='Brasil', max_length=32, null=True)),
                ('cpais', models.CharField(blank=True, default='1058', max_length=5, null=True)),
                ('municipio', models.CharField(blank=True, max_length=64, null=True)),
                ('cmun', models.CharField(blank=True, max_length=9, null=True)),
                ('cep', models.CharField(blank=True, max_length=16, null=True)),
                ('uf', models.CharField(blank=True, choices=[('AL', 'ALAGOAS')], max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now=True, verbose_name='Data de Criação')),
                ('data_edicao', models.DateTimeField(auto_now=True, verbose_name='Data de Edição')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('tipoPessoa', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2)),
                ('informacoes_adicionais', models.CharField(blank=True, max_length=1055, null=True)),
                ('email_padrao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email_padrao', to='pessoa.email')),
                ('endereco_padrao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endereco_padrao', to='pessoa.endereco')),
                ('id_Empresa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Id_empresa_pessoa', to='empresaColigada.empresa')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoa.pessoa')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('cpf', models.CharField(blank=True, max_length=32, null=True, verbose_name='Cpf')),
                ('rg', models.CharField(blank=True, max_length=32, null=True, verbose_name='RG')),
                ('nascimento', models.DateField(blank=True, null=True, verbose_name='Nascimenot')),
            ],
            options={
                'verbose_name': 'Pessoa Física',
                'verbose_name_plural': 'Pessoas Física',
            },
            bases=('pessoa.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoa.pessoa')),
                ('cnpj', models.CharField(blank=True, max_length=32, null=True, verbose_name='Cnpj')),
                ('razao', models.CharField(blank=True, max_length=255, null=True, verbose_name='Razão')),
                ('nome_fantasia', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome Fantasia')),
                ('inscricaoEstadual', models.CharField(blank=True, max_length=32, null=True, verbose_name='Incrição Estadual')),
                ('responsavel', models.CharField(blank=True, max_length=32, null=True, verbose_name='Responsável')),
                ('situcao_fiscal', models.CharField(blank=True, choices=[('LR', 'Lucro Real'), ('LP', 'Lucro Presumido'), ('SN', 'Simples Nacional'), ('SE', 'Simples Nacional, , excesso sublimite de receita bruta')], max_length=2, null=True)),
                ('suframa', models.CharField(blank=True, max_length=16, null=True, verbose_name='Suframa')),
            ],
            options={
                'verbose_name': 'Pessoa Jurídica',
                'verbose_name_plural': 'Pessoas Jurídica',
            },
            bases=('pessoa.pessoa',),
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_telefone', models.CharField(blank=True, choices=[('FIX', 'Fixo'), ('CEL', 'Celular'), ('FAX', 'Fax'), ('OUT', 'Outro')], max_length=8, null=True)),
                ('telefone', models.CharField(max_length=32)),
                ('pessoaTelefone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone', to='pessoa.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=255)),
                ('pessoa_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site', to='pessoa.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='site_padrao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='site_padrao', to='pessoa.site'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='telefone_padrao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telefone_padrao', to='pessoa.telefone'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='usuario_criacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pessoa_end',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to='pessoa.pessoa'),
        ),
        migrations.AddField(
            model_name='email',
            name='pessoa_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='pessoa.pessoa'),
        ),
    ]
