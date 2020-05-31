using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using PagedList;
using se_liga_mogi.Models;

namespace se_liga_mogi.Controllers
{
    public class diarias_e_passagensController : Controller
    {
        private Se_Liga_MogiEntities1 db = new Se_Liga_MogiEntities1();
        public ActionResult Index(int pagina = 1, string Pesquisa = "")
        {
            var q = db.diarias_e_passagens.AsQueryable();
            if (!string.IsNullOrEmpty(Pesquisa))
            {
                q = q.Where(c => c.motivo.Contains(Pesquisa));
            }
            q = q.OrderBy(c => c.data_inicio);
            ViewBag.CurrentSort = Pesquisa;
            return View(q.ToPagedList(pagina, 10));
        }
    }
}
