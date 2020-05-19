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
    public class servidoresController : Controller
    {
        private Se_Liga_MogiEntities1 db = new Se_Liga_MogiEntities1();
        public ActionResult Index(int pagina = 1, string Pesquisa = "")
        {
            var q = db.servidores.AsQueryable();
            if (!string.IsNullOrEmpty(Pesquisa))
            {
                q = q.Where(c => c.nome_servidor.Contains(Pesquisa));
            }
            q = q.OrderBy(c => c.nome_servidor);
            return View(q.ToPagedList(pagina, 10));
        }
        public ActionResult Detalhes(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            servidores servidores = db.servidores.Find(id);
            if (servidores == null)
            {
                return HttpNotFound();
            }
            return View(servidores);
        }
    }
}
