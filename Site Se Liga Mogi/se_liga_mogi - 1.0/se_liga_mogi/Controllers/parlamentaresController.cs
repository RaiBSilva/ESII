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
    public class parlamentaresController : Controller
    {
        private Se_Liga_MogiEntities1 db = new Se_Liga_MogiEntities1();

        public ActionResult Index(int pagina = 1, string Pesquisa = "")
        {
            var q = db.parlamentares.AsQueryable();
            if (!string.IsNullOrEmpty(Pesquisa))
            {
                q = q.Where(c => c.nome_parlamentar.Contains(Pesquisa));
            }
            q = q.OrderBy(c => c.nome_parlamentar);
            ViewBag.CurrentSort = Pesquisa;
            return View(q.ToPagedList(pagina, 10));
        }

        public ActionResult Detalhes(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }

            parlamentares parlamentares= db.parlamentares.Find(id);

            if (parlamentares == null)
            {
                return HttpNotFound();
            }

            return View(parlamentares);
        }
        public ActionResult Presenca(int pagina = 1)
        {
            var q = db.presenca_parlamentares.AsQueryable();
            return View(q.ToPagedList(pagina, 10));

            //presenca_parlamentares presenca = db.presenca_parlamentares.Find(id);
            //ViewBag.nomeParlamentar = parlamentares.nome_parlamentar;
            //return View(presenca);
        }
    }
}
