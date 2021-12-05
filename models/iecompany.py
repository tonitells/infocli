# -*- coding: utf-8 -*-
from odoo import models , fields , api , _

class iecompany(models.Model):
    _name = 'infocli.iecompany'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Empresas I/E'
    _rec_name = 'name'
    _order = "name"
    #COmentari
    name = fields.Char(string='Empresa',default='' , tracking=True)
    origin = fields.Char(string='Origen',default='' )
    data_carga = fields.Datetime(string='Fecha Carga', default=lambda self: fields.datetime.now())
