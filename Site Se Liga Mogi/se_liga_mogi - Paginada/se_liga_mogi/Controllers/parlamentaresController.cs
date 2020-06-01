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
<<<<<<< HEAD
=======

>>>>>>> bba4e350deae07d0d0ec12c2673c737beec46a7c
        public ActionResult Detalhes(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
<<<<<<< HEAD
            parlamentares parlamentares= db.parlamentares.Find(id);
=======
            parlamentares parlamentares = db.parlamentares.Find(id);
>>>>>>> bba4e350deae07d0d0ec12c2673c737beec46a7c
            if (parlamentares == null)
            {
                return HttpNotFound();
            }
<<<<<<< HEAD
            return View(parlamentares);
        }
        public ActionResult Presenca(int pagina = 1)
        {
            var q = db.presenca_parlamentares.AsQueryable();
            return View(q.ToPagedList(pagina, 10));
=======
            presenca_parlamentares presenca = db.presenca_parlamentares.Find(id);
            ViewBag.nomeParlamentar = parlamentares.nome_parlamentar;
            return View(presenca);
>>>>>>> bba4e350deae07d0d0ec12c2673c737beec46a7c
        }
    }
}
