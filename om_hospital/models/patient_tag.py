# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "Patient Tag"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color 2")
    sequence = fields.Integer(string="Sequence")

    #name değeri daha önce kayıtlı ise yeni kayıt oluşturmuyor
    #('unique_tag_name', 'unique (name)', 'Name must be unique')
    #name değeri daha önceden kayıtlı ve aktif olan bir kayıt varsa yeni kayıt oluşturmuyor
    #('unique_tag_name', 'unique (name,active)', 'Name must be unique')
    #Yeni kayıt esnaısnda squence değeri sıfırdan küçükse kabul etme
    #('check_sequence', 'check (sequence > 0)', 'Sequence must be non zero positive number.')
    _sql_constraints = [
        ('unique_tag_name', 'unique (name,active)', 'Name must be unique.'),
        ('check_sequence', 'check (sequence > 0)', 'Sequence must be non zero positive number.')
    ]