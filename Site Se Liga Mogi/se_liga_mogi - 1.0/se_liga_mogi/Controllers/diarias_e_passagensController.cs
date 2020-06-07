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
        public ActionResult Index(
            int pagina = 1,
            string Pesquisa = "",
            int? Min = null,
            int? Max = null,
            DateTime? DataMin = null,
            DateTime? DataMax = null
        )

        {
            var q = db.diarias_e_passagens.AsQueryable();
            if (!string.IsNullOrEmpty(Pesquisa))
            {
                q = q.Where(c => c.motivo.Contains(Pesquisa));
            }
            q = q.OrderBy(c => c.data_inicio);

            if (Min != 0) {
                q = q.Where(c => c.valor > Min);
            }

            if (Max != 0)
            {
                q = q.Where(c => c.valor < Min);
            }

            if (DataMin != DateTime.MinValue)
            {
                q = q.Where(c => c.data_inicio > DataMin);
            }

            if (DataMax != DateTime.MinValue)
            {
                q = q.Where(c => c.data_fim > DataMax);
            }
            
            ViewBag.Pesquisa = Pesquisa;
            ViewBag.Min = Min;
            ViewBag.Max = Max;
            ViewBag.DataMin = DataMin;
            ViewBag.DataMax = DataMax;
            return View(q.ToPagedList(pagina, 10));
        }
    }
}
