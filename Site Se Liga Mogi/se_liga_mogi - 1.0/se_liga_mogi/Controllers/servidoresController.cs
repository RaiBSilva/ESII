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
        public ActionResult Index(
            int pagina = 1,
            string Pesquisa = "",
            string Filtro = "",
            int? min = 0,
            int? max = 100000)
        {
            var q = db.servidores.AsQueryable();
            if (!string.IsNullOrEmpty(Pesquisa))
            {
                q = q.Where(c => c.nome_servidor.Contains(Pesquisa));
            }
            if (!string.IsNullOrEmpty(Filtro))
            {
                switch (Filtro)
                {
                    case "s":
                        if (min != null) {
                            q = q.Where(c => c.salario_servidor > min);
                        }
                        if (max != null) {
                            q = q.Where(c => c.salario_servidor < max);
                        }
                        break;
                    case "d":
                        if (min != null)
                        {
                            q = q.Where(c => c.descontos_servidor > min);
                        }
                        if (max != null)
                        {
                            q = q.Where(c => c.descontos_servidor < max);
                        }
                        break;
                    case "r":
                        if (min != null)
                        {
                            q = q.Where(c => c.salario_liquido_servidor > min);
                        }
                        if (max != null)
                        {
                            q = q.Where(c => c.salario_liquido_servidor < max);
                        }
                        break;
                    default:
                        return HttpNotFound();
                }
            }
            q = q.OrderBy(c => c.salario_liquido_servidor);
            ViewBag.CurrentSort = Pesquisa;
            ViewBag.FiltroAtual = Filtro;
            ViewBag.Min = min;
            ViewBag.Max = max;
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
