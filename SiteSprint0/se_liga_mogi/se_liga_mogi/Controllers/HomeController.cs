using se_liga_mogi.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;

namespace se_liga_mogi.Controllers
{
    public class HomeController : Controller
    {
        private Se_Liga_MogiEntities db = new Se_Liga_MogiEntities();
        public ActionResult Index(string Pesquisa = "")
        {
            var q = db.servidores.AsQueryable();
            if (!string.IsNullOrEmpty(Pesquisa))
            {
                q = q.Where(c => c.rgf.Contains(Pesquisa));
            }
            q = q.OrderBy(c => c.rgf);
            return View(q.ToList());
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