# -*- coding: utf-8 -*-
# Copyright 2018 Oktovan Rezman
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class RoadmapQuarter(models.Model):
    _name = "roadmap.quarter"
    _description = "Roadmap Quarter"

    name = fields.Char(
        string="Quarter",
        required=True,
    )

    todo=fields.Text(
    	string="Todo",
    	required=True,
    )

    pic = fields.Many2one(
        string="PIC",
        comodel_name="hr.employee",
        required=True,
    )


