using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using System.Web.UI;
using se_liga_mogi.Models;
using PagedList;

namespace se_liga_mogi.Controllers
{
    public class projetos_de_leiController : Controller 
    {
        private Se_Liga_MogiEntities1 db = new Se_Liga_MogiEntities1();
        public ActionResult Index(int pagina = 1, string Pesquisa = "")
        {
            var q = db.projetos_de_lei.AsQueryable();
            if (!string.IsNullOrEmpty(Pesquisa))
            {
                q = q.Where(c => c.autor_projeto.Contains(Pesquisa));
            }
            q = q.OrderBy(c => c.autor_projeto);
            ViewBag.CurrentSort = Pesquisa;
            return View(q.ToPagedList(pagina, 10));
        }
        public ActionResult Detalhes(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            projetos_de_lei projetos_de_lei = db.projetos_de_lei.Find(id);
            if (projetos_de_lei == null)
            {
                return HttpNotFound();
            }
            return View(projetos_de_lei);
        }
    }
}
