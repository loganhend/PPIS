#include"doc.h"

using namespace std;

//All for file
File::File(const string& f_heading, const string& author, const time_t& cD) : heading(f_heading), author(author), creationDate(cD) {};

const string File::getHeading()
{
	return this->heading;
}

const string File::getAuthor()
{
	return this->author;
}

const time_t File::getCD()
{
	return this->creationDate;
}

void File::setHeading(const string& head)
{
	this->heading = head;
}


//All for Illustrations

Illustration::Illustration(const string& head, const string& author, const time_t& cD) : File(head, author, cD) {};


//All for Doc

Document::Document(const string& head, const string& author, const time_t& cD, const string& text) : text(text), File(head, author, cD) {};

void Document::UpdHeading(const string& head)
{
	this->heading = head;
}

void Document::UpdText(const string& text)
{
	this->text = text;
}

void Document::LinkIllustration(shared_ptr<Illustration> ill)
{
	if ((this->illustrations).find(ill) == (this->illustrations).end())
		(this->illustrations).insert(ill);
	else throw invalid_argument("Illustration is already in the document");
}

void Document::UnlinkIllustration(shared_ptr<Illustration> ill)
{
	if ((this->illustrations).find(ill) != (this->illustrations).end())
		(this->illustrations).erase(ill);
	else throw invalid_argument("Illustration is not in the document");
}

//All for catalog
Catalog::Catalog(const string& name) : name(name) {};


void Catalog::addFile(shared_ptr<File> new_file)
{
	if ((this->files).find(new_file) == (this->files).end())
		(this->files).insert(new_file);
	else throw invalid_argument("File is alredy in the catalog");
}

void Catalog::addCatalog(shared_ptr<Catalog> new_catalog)
{
	if ((this->catalogs).find(new_catalog) == (this->catalogs).end())
		(this->catalogs).insert(new_catalog);
	else throw invalid_argument("Catalog is alredy in the catalog");
}

void Catalog::deleteFile(shared_ptr<File> file)
{
	if ((this->files).find(file) != (this->files).end())
		(this->files).erase(file);
	else throw invalid_argument("File is not in the catalog");
}

void Catalog::deleteCatalog(shared_ptr<Catalog> catalog)
{
	if ((this->catalogs).find(catalog) != (this->catalogs).end())
		(this->files).erase(catalog);
	else throw invalid_argument("Catalog is not in the catalog");
}

set<shared_ptr<File>> Catalog::getFiles() const 
{
	return this->files;
}

set<shared_ptr<Catalog>> Catalog::getCatalogs() const
{
	return this->catalogs;
}

//All for Buffer
Buffer::Buffer()
{
	bufferCatalog = make_unique<Catalog>(Catalog("Buffer catalog"));
	mainCatalog = make_unique<Catalog>(Catalog("Main catalog"));
}

shared_ptr<Catalog> Buffer::getBuffer() const
{
	return bufferCatalog;
}

shared_ptr<Catalog> Buffer::getMain() const
{
	return mainCatalog;
}

void Buffer::addFile(shared_ptr<File> file)
{
	this->bufferCatalog->addFile(file);
}

//Actor
Actor::Actor(const string& n, shared_ptr<Buffer> buf) : name(n), buffer(buf) {};

//Illustrator

Illustrator::Illustrator(const string& n, shared_ptr<Buffer> buf) : Actor(n,buf) {};

void Illustrator::CreateIllustration(const string& head) 
{
	buffer->addFile(make_shared<Illustration>(head, name));
}

void Illustrator::AddIllustrationToCatalog(shared_ptr<Illustration> ill, shared_ptr<Catalog> catalog) 
{
	catalog->addFile(ill);
}

void Illustrator::DeleteIllustration(shared_ptr<Illustration> ill, shared_ptr<Catalog> catalog) 
{
	catalog->deleteFile(ill);
	for (auto sub_cat : catalog->getCatalogs()) {
		DeleteIllustration(ill, sub_cat);
	}
}

void Illustrator::DeleteIllustration(std::shared_ptr<Illustration> ill) 
{
	DeleteIllustration(ill, buffer->getMain());
}

//Writer

Writer::Writer(const string& n, shared_ptr<Buffer> buf) : Actor(n, buf) {};

void Writer::CreateDocument(const string& head, const string& text) 
{
	buffer->getBuffer()->addFile(make_shared<Document>(head, text));
}

void Writer::UpdateDocumentHeading(const string& head, shared_ptr<Document> doc) 
{
	doc->UpdHeading(head);
}

void Writer::UpdateDocumentText(const string& text, shared_ptr<Document> doc) 
{
	doc->UpdText(text);
}

void Writer::LinkIllustration(shared_ptr<Document> doc, shared_ptr<Illustration> ill) 
{
	doc->LinkIllustration(ill);
}

void Writer::UnlinkIllustration(shared_ptr<Document> doc, shared_ptr<Illustration> ill)
{
	doc->UnlinkIllustration(ill);
}

//Secretary

Secretary::Secretary(const string& n, shared_ptr<Buffer> buf) : Actor(n, buf) {};

void Secretary::AddFileToCatalog(shared_ptr<File> file, shared_ptr<Catalog> catalog)
{
	catalog->addFile(file);
}

shared_ptr<Document> Secretary::FindDocument(const string& author, shared_ptr<Catalog> catalog)
{
	for (shared_ptr<Document> file : catalog->getFiles()) {
		if((file->getAuthor()==author))
			return file;
	}

	for (auto sub_cat : catalog->getCatalogs()) {
		FindDocument(author, sub_cat);
	}
}

shared_ptr<Document> Secretary::FindDocument(const string& heading, shared_ptr<Catalog> catalog)
{
	for (shared_ptr<Document> file : catalog->getFiles()) {
		if ((file->getHeading() == heading))
			return file;
	}

	for (auto sub_cat : catalog->getCatalogs()) {
		FindDocument(heading, sub_cat);
	}
}

//Administrator
Administrator::Administrator(const string& n, shared_ptr<Buffer> buf) : Actor(n, buf) {};

void Administrator::CreateCatalog(const string& name, shared_ptr<Catalog> headCatalog) 
{
	headCatalog->addCatalog(make_unique<Catalog>(Catalog(name)));
}

void Administrator::MoveFileToCatalog(shared_ptr<File> file, shared_ptr<Catalog> newCatalog, shared_ptr<Catalog> oldCatalog)
{
	newCatalog->addFile(file);
	oldCatalog->deleteFile(file);
}

void Administrator::DeleteFile(shared_ptr<File> file, shared_ptr<Catalog> headCatalog)
{
	headCatalog->deleteFile(file);
	for (auto sub_cat : headCatalog->getCatalogs()) {
		DeleteFile(file, sub_cat);
	}
}